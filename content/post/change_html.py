#!/usr/bin/env python3
import sys
import argparse
import re

try:
    from bs4 import BeautifulSoup, Tag, NavigableString
    HAVE_BS4 = True
except Exception as e:
    HAVE_BS4 = False

def detect_parser():
    try:
        import lxml  # noqa: F401
        return "lxml"
    except Exception:
        return "html.parser"

def is_data_uri(url: str) -> bool:
    return bool(url) and url.strip().lower().startswith("data:")

def extract_image_url(wrapper_div: "Tag") -> str:
    # Try child <img data-original>
    img = wrapper_div.find("img")
    if img:
        data_original = img.get("data-original")
        if data_original and not is_data_uri(data_original):
            return data_original.strip()
        # fallback to img src if not a data URI
        img_src = img.get("src")
        if img_src and not is_data_uri(img_src):
            return img_src.strip()
    # Try wrapper's href (some content puts href on the div for fancybox)
    href = wrapper_div.get("href") or wrapper_div.get("data-href")
    if href and not is_data_uri(href):
        return href.strip()
    return ""

def extract_caption_text(ancestor_figure: "Tag") -> str:
    if not ancestor_figure:
        return ""
    cap = ancestor_figure.find("figcaption")
    if not cap:
        return ""
    # Get plain text and strip excessive whitespace
    text = cap.get_text(separator=" ", strip=True)
    return text

def closest_ancestor(tag: "Tag", names):
    cur = tag
    while cur and cur.name not in names:
        cur = cur.parent
    return cur

def make_simple_figure(soup: "BeautifulSoup", src_url: str, caption_text: str, width_percent: int) -> "Tag":
    fig = soup.new_tag("figure", **{"class": "wp-block-image"})
    img = soup.new_tag("img", src=src_url, alt="")
    img["style"] = f"width: {width_percent}%;"
    fig.append(img)
    fc = soup.new_tag("figcaption")
    fc.string = caption_text or ""
    fig.append(fc)
    return fig

def process_html(html: str, width_percent: int = 40) -> str:
    if not HAVE_BS4:
        sys.stderr.write("Error: beautifulsoup4 is required. Install with `pip install beautifulsoup4 lxml`.\n")
        sys.exit(2)

    parser = detect_parser()
    soup = BeautifulSoup(html, parser)

    # Find all fancybox/lazyload wrappers
    wrappers = soup.find_all("div", class_=lambda c: c and "fancybox-wrapper" in c)
    # Keep original order; we'll insert new figures adjacent to ancestors
    for w in list(wrappers):
        # Determine outer ancestor to replace/append near
        ancestor = closest_ancestor(w, {"figure"})
        gallery_ancestor = None
        if ancestor and ancestor.has_attr("class"):
            classes = " ".join(ancestor.get("class", []))
            if "wp-block-gallery" in classes:
                gallery_ancestor = ancestor

        # Get caption from nearest figure ancestor (if any)
        caption_text = extract_caption_text(ancestor)

        # Extract image URL
        src = extract_image_url(w)
        if not src:
            # Nothing usable; skip
            continue

        # Build new simple figure
        simple_fig = make_simple_figure(soup, src, caption_text, width_percent)

        # Insert the new figure:
        if gallery_ancestor:
            # If inside a gallery, insert after the gallery and later clean up
            gallery_ancestor.insert_after(simple_fig)
        elif ancestor:
            ancestor.insert_after(simple_fig)
        else:
            # No figure ancestor; just replace wrapper itself
            w.insert_after(simple_fig)

        # Remove the old structure: remove its figure ancestor if it exists,
        # otherwise remove the wrapper itself.
        if ancestor:
            ancestor.decompose()
        else:
            w.decompose()

    # Clean up empty gallery figures that may remain without images
    for gal in soup.find_all("figure", class_=lambda c: c and "wp-block-gallery" in c):
        # If gallery no longer contains <img>, remove it
        if not gal.find("img"):
            gal.decompose()

    # Optional: collapse multiple consecutive blank lines
    out = str(soup)
    out = re.sub(r"\n\s*\n\s*\n+", "\n\n", out, flags=re.MULTILINE)
    return out

def main():
    ap = argparse.ArgumentParser(description="Convert WordPress fancybox/lazyload image blocks to simple <figure><img><figcaption>.")
    ap.add_argument("input", nargs="?", help="Input HTML file (default: STDIN)")
    ap.add_argument("-o", "--output", help="Output HTML file (default: STDOUT)")
    ap.add_argument("--width", type=int, default=40, help="Image width percentage for inline style (default: 40)")
    args = ap.parse_args()

    # Read input
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            html = f.read()
    else:
        html = sys.stdin.read()

    result = process_html(html, width_percent=args.width)

    # Write output
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        sys.stdout.write(result)

if __name__ == "__main__":
    main()

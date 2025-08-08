---
title: GNU Radio OOT
author: jie
type: post
date: 2022-04-10T11:52:25+00:00
excerpt: 有关 GNU Radio OOT 的一些笔记，有关 work 怎么写
url: /2022/04/10/gnu-radio-oot/
argon_hide_readingtime:
  - 'false'
argon_meta_simple:
  - 'false'
argon_first_image_as_thumbnail:
  - default
argon_show_post_outdated_info:
  - default
views:
  - 1783
categories:
  - 资料

---
GNU Radio OOT, Out Of Tree Modules

<div style="height:21px" aria-hidden="true" class="wp-block-spacer">
</div>

#### 安装 gnuradio

不会  
我装的版本是 3.10，在 ubuntu 22.04 上

#### 什么是 OOT

就是自己写 gnuradio 的 block

<div style="height:21px" aria-hidden="true" class="wp-block-spacer">
</div>

#### 怎么写

  1. 参考官方教程 <a href="https://wiki.gnuradio.org/index.php/OutOfTreeModules" target="_blank" rel="noreferrer noopener">https://wiki.gnuradio.org/index.php/OutOfTreeModules</a>  
    真的是这些 wiki 都怎么写的，懂的都懂，不懂的就是不懂，
  2. 参考这篇中文的 <a href="https://blog.csdn.net/Flag_ing/article/details/118568932" target="_blank" rel="noreferrer noopener">https://blog.csdn.net/Flag_ing/article/details/118568932</a>  
    大约就是上一篇的中文翻译，建议看这个吧，我觉得不是我英文差看不懂上面那个
  3. 本质上就是写 C++，改 `lib/block_name.cc` 这个文件，自己的 C++ 函数写好套个壳，壳怎么套参考上面两点
  4. 具体怎么写 `lib/block_name.cc` 建议参考 gnuradio 自带的 block 的写法

哎可能是用的人太少了，都没什么教程

<div style="height:21px" aria-hidden="true" class="wp-block-spacer">
</div>



以下内容算笔记

#### 添加 arguments

在添加新 block 时就设置 arguments 类型和名称，比如 `int arg1, float arg2`

如果添加新 block 时没有写，后期想加，很麻烦，得手动改

<pre class="wp-block-code"><code>gr-howto$ gr_modtool add -t general -l cpp square_ff
GNU Radio module name identified: howto
Language: C++
Block/code identifier: square_ff
Enter valid argument list, including default arguments: </code></pre>

<div style="height:21px" aria-hidden="true" class="wp-block-spacer">
</div>

#### OOT 核心

就是 `block_name_impl::general_work`

gnuradio 是个 streaming 的系统，但并不是进一个 sample 就处理一个，而是有一个 buffer。buffer 的大小就是下面这个例子里的 `i < noutput_items`, `noutput_items`的大小大概几千吧（不确定）。当这个 buffer 都 consume 完后，就再进来一个大小类似的 buffer。（我猜的）

<pre class="wp-block-code"><code>    int
    square_ff_impl::general_work (int noutput_items,
                                  gr_vector_int &ninput_items,
                                  gr_vector_const_void_star &input_items,
                                  gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items&#91;0];
      float *out = (float *) output_items&#91;0];

      for(int i = 0; i &lt; noutput_items; i++) {
        out&#91;i] = in&#91;i] * in&#91;i];
      }
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }</code></pre>



<div style="height:21px" aria-hidden="true" class="wp-block-spacer">
</div>

#### 关于 work

##### work 是什么

  * 先看这个 wiki <a href="https://wiki.gnuradio.org/index.php/Types_of_Blocks" target="_blank" rel="noreferrer noopener">https://wiki.gnuradio.org/index.php/Types_of_Blocks</a>  
    然后你会觉得你懂了，但是你不懂
  * 大概就是指定输入输出的速度比例

##### work 的类型

  * 在添加 block 时就需要指定 block 的类型
  * `$ gr_modtool add -t general -l cpp some_name`  
    -t 后面
  * 后期要改怎么办：我不会，删了重新添加
  * `-t` 后面指定 block 的类型，我也不知道剩下的是啥 sink|source|sync|decimator|interpolator|general|tagged_stream|hier|noblock

**具体类型：**

**Synchronous Blocks** (1:1): `-t sync`

  * One input, one output
  * 比如上面那个 `square_ff` 的例子，其实用 `square_ff_impl::work` 就行



**Decimation Blocks** (N:1): `-t decimator`

  * N input, 1 output
  * 需要设置下面这个`decimation`的值  
    比如 1024 个 input，1 output，第四个变量就写 1024，这样的话，gnuradio 的 buffer 就必然是 1024 的倍数（我猜的）

<pre class="wp-block-code"><code>  #include &lt;gr_sync_decimator.h&gt;

  class my_decim_block : public gr_sync_decimator
  {
  public:
    my_decim_block(...):
      gr_sync_decimator("my decim block", 
                        in_sig,
                        out_sig,
                        decimation)
    {
      //constructor stuff
    }
    //work function here...
  };</code></pre>



**Interpolation Blocks** (1:M): `-t interpolator`

  * 同上，没写过



**Basic (a.k.a. General) Blocks** (N:M): `-t general`

  * 不会
  * wiki 里竟然这么写，observations？？？ 我真的无语

<pre class="wp-block-code"><code>Some observations:

· This class overloads the general_work() method, not work()
· The general work has a parameter: ninput_items
    · ninput_items is a vector describing the length of each input buffer
· Before return, general_work must manually consume the used inputs
· The number of items in the input buffers is assumed to be noutput_items
    ·This behaviour can be altered by overloading the forecast() method but is not mandatory</code></pre>

  * 我试过，没成功过  
    比如 1024 input，1 output 情况下，必须保证 `ninput_items[0]`是 1024 的倍数，应当在 `forecast` 中写一些东西（我不会）  
    如果不写的话，`ninput_items[0]` 等于 5000（比如），这样的话，前 4 个 output 会是正确的，后 5000 &#8211; 1024*4 个 input 会 pad 一些 0 到 1024 长，计算 output，结果会不对。（我猜的）



<div style="height:21px" aria-hidden="true" class="wp-block-spacer">
</div>

##### 不同类型的 work 怎么写

建议参考 gnuradio 自己的模块，看上面的 wiki 链接是不会懂的

  * **Decimation**  
    参考 <a href="https://github.com/gnuradio/gnuradio/blob/main/gr-blocks/lib/pack_k_bits_bb_impl.cc" target="_blank" rel="noreferrer noopener">gnuradio/gr-blocks/lib/pack_k_bits_bb_impl.cc</a>  
    k input, 1 output  
    不懂 `d_pack(k)` 是干什么用的

<pre class="wp-block-code"><code>  pack_k_bits_bb_impl::pack_k_bits_bb_impl(unsigned k)
      : sync_decimator("pack_k_bits_bb",
                       io_signature::make(1, 1, sizeof(unsigned char)),
                       io_signature::make(1, 1, sizeof(unsigned char)),
                       k),
        d_pack(k)
  {
      d_k = k;
      set_tag_propagation_policy(TPP_CUSTOM);
  }

  int pack_k_bits_bb_impl::work(int noutput_items,
                                gr_vector_const_void_star& input_items,
                                gr_vector_void_star& output_items)
  {
      const unsigned char* in = (const unsigned char*)input_items&#91;0];
      unsigned char* out = (unsigned char*)output_items&#91;0];
      d_pack.pack(out, in, noutput_items);
      return noutput_items;
  }

  } /* namespace blocks */
  } /* namespace gr */</code></pre>

`pack` 怎么写的在这里 <a href="https://github.com/gnuradio/gnuradio/blob/main/gr-blocks/lib/pack_k_bits.cc" target="_blank" rel="noreferrer noopener">https://github.com/gnuradio/gnuradio/blob/main/gr-blocks/lib/pack_k_bits.cc</a>

<pre class="wp-block-code"><code>  for i &lt; noutput_items:
      for j &lt; k:
          in&#91;i * k + j] 一些计算
      out&#91;i] = xxx</code></pre>

因为保证了`noutput_items`是 k 的倍数，所以就可以这么写，这么简单我居然想不到（x）

虽然我觉得把这两个 for 放到上面 `impl.cc` 里是不是合理一点

<pre class="wp-block-code"><code>  void pack_k_bits::pack(unsigned char* bytes, const unsigned char* bits, int nbytes) const
  {
      for (int i = 0; i &lt; nbytes; i++) {
          bytes&#91;i] = 0x00;
          for (unsigned int j = 0; j &lt; d_k; j++) {
              bytes&#91;i] |= (0x01 & bits&#91;i * d_k + j]) &lt;&lt; (d_k - j - 1);
          }
      }
  }</code></pre>

  * **Interpolation**  
    不会  
    <a href="https://github.com/BogdanDIA/gr-dvbt/blob/master/lib/convolutional_interleaver_impl.cc" target="_blank" rel="noreferrer noopener">https://github.com/BogdanDIA/gr-dvbt/blob/master/lib/convolutional_interleaver_impl.cc</a>，七年前，我猜 `sync_interpolator` 现在已经不用了
  * **General work**  
    pack 用的 decimation，unpack 用的 general work，想不到吧 <a href="https://github.com/gnuradio/gnuradio/blob/main/gr-blocks/lib/packed_to_unpacked_impl.cc" target="_blank" rel="noreferrer noopener">https://github.com/gnuradio/gnuradio/blob/main/gr-blocks/lib/packed_to_unpacked_impl.cc</a> 改了`forecast`，我不会



<div style="height:21px" aria-hidden="true" class="wp-block-spacer">
</div>

#### 编译错误怎么办

  * 我根本搞不懂 cmakelists.txt 怎么写
  * 如果出问题

  1. build 下，`$ make clean`
  2. module 目录下 `$ gr_modtool bind block_name`
  3. 重新 make

  * 有时候 `make install` 没问题，但是实际运行 block 时出错，那就是 c++ 的问题了，c++ 太难了

github 想搜点别人写的例子，搜出来全是 folk gnuradio 的 gnuradio，烦死了，folk 有用吗，能直接安装吗
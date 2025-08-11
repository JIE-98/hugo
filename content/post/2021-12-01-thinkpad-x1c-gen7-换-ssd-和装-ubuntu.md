---
title: ThinkPad x1c gen7 换 SSD 和装 ubuntu
author: jie
type: post
date: 2021-12-01T13:11:45+00:00
excerpt: |
  因为换了块 SSD，顺便装一下 ubuntu。原来的 8G + 256G 真的是丐中丐，2021 年了太难受了好吧。
  买的三星 EVO 970 EVO PLUS，1T 的。
url: /2021/12/01/thinkpad-x1c-gen7-换-ssd-和装-ubuntu/
argon_hide_readingtime:
  - 'false'
argon_meta_simple:
  - 'false'
argon_first_image_as_thumbnail:
  - 'false'
argon_show_post_outdated_info:
  - default
views:
  - 2461
categories:
  - 生活
tags:
  - 电子产品

---
因为换了块 SSD，顺便装一下 ubuntu  
原来的 8G + 256G 真的是丐中丐，2021 年了太难受了好吧  
买的三星 EVO 970 EVO PLUS，1T 的。德亚 89 欧，运到瑞典就要 95 欧 +5 欧运费。在瑞亚买了一天德亚就降价了 20 欧，只好退了再买，然后瑞亚也降了，无语。

## 安装新 SSD

  1. 备份  
    旧 SSD 里也就几十G的东西，拷拷很快的
  2. 做U盘启动盘，<a data-wplink-edit="true" href="https://www.microsoft.com/zh-cn/software-download/windows10">https://www.microsoft.com/zh-cn/software-download/windows10</a>  
    上面说要 8G 的空间，但实际上装完就 5G，我觉得应该 8G 大小的U盘够了，我猜的。装的是家庭中文版，因为我知道我的是家庭中文版。之后安装完后需要激活 windows，用的激活码应该在注册表里。
  3. 断电  
    把充电器拔了，进 BIOS 选彻底断电。我看也有人拆了后盖之后把电池的线断开的。
  4. 换 SSD  
    一直不敢掰有卡扣的，铰链那条边是螺丝拧下来就松开了，两条短边用塑料片把卡扣撬开，最后一条边用力向上掰。原来底板是金属的。装回去的时候螺丝掉了个垫片，算了。  
    打开来发现几根猫毛，铰链粘了好多灰。  
    原来是有散热贴的，可是为什么是朝向主板那一面。新的 SSD 背面有个厚贴纸，不知道是啥，没撕，可能是散热用的吧，上面写着撕了就不给保修，要是有人去保修 SSD 也太惨了吧。
  5. 装 win10  
    U盘插进去装就完事了，好快，大概也就 10 分钟就开机了。然后进设置激活一下。

<!-- <div class="wp-block-image">
  <figure class="aligncenter size-large is-resized">
  
  <div class='fancybox-wrapper lazyload-container-unload' data-fancybox='post-images' href='http://apodized.com/wp-content/uploads/2021/12/20211206154455-1024x857.jpg'>
    <img class="lazyload lazyload-style-1" src="data:image/svg+xml;base64,PCEtLUFyZ29uTG9hZGluZy0tPgo8c3ZnIHdpZHRoPSIxIiBoZWlnaHQ9IjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3Ryb2tlPSIjZmZmZmZmMDAiPjxnPjwvZz4KPC9zdmc+"  loading="lazy" data-original="http://apodized.com/wp-content/uploads/2021/12/20211206154455-1024x857.jpg" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAANSURBVBhXYzh8+PB/AAffA0nNPuCLAAAAAElFTkSuQmCC" alt="" class="wp-image-202" width="512" height="429"  sizes="(max-width: 512px) 100vw, 512px" />
  </div><figcaption>这个白色应该是散热贴吧？里面好多悉悉索索的东西，应该是人渣吧</figcaption></figure>
</div> -->

<figure class="wp-block-image">
  <img src="https://static.apodized.com/wp-content/uploads/2021/12/20211206154455-1024x857.jpg" alt="" style="width: 80%;">
  <figcaption>这个白色应该是散热贴吧？里面好多悉悉索索的东西，应该是人渣吧</figcaption>
</figure>

## 装 win10 专业版

按照传统去淘宝花 8 块大洋买了 pro 版本的激活码，激活了。然而还是改不了语言。  
然后又去淘宝从镜像装了 pro 版本，好慢好慢好慢好慢。装完之后记事本文件打不开，奸商让我重装，我真的好无语。可能我就是盗版软件的受害者吧，在设置里把记事本卸载重装就行了。  
装完感觉我电脑中文字题显示有问题，算了，不想搞。

## 其他

重装完我发现我的油猴脚本没了，原来默认是没备份的啊，我以为会跟着谷歌账号走呢。其实也无所谓，反正都是用的别人的没有我自己写的。  
发现 Typora 居然要收费了，然后文档里的图片全没了，因为默认保存在 `"C:\Users\用户名\AppData\Roaming\Typora\typora-user-images"`这种地方，显然我没注意备份。算了。感觉在本地写文档很容易丢内容，一不小心剪切一下都没了，不像 google doc 有历史版本。

### 装 ubuntu 双系统

就参考的这个：[链接][1]{.wp-editor-md-post-content-link} ，看这个就行了

  1. 装启动盘
  2. SSD 分一下区  
    分了 300G 也不知道够不够用
  3. 关闭 secure boot 和 fast boot  
    我也不知道要不要关，反正我关了，关闭 secure boot 之后要输入 BitLocker 密钥，我也不知道是什么。
  4. 从U盘启动  
    先关机，然后按 Enter，然后 F12 选择启动方式。
  5. 装 ubuntu  
    装就是了，在之前分出来的地方分两个区，`/boot`&nbsp;和<span style="font-size: revert; color: initial;">&nbsp;</span>`/`&nbsp;。
  6. 剩下的  
    把 secure boot 打开。  
    我装完默认是从 ubuntu 启动。我不会改启动顺序，我的 BIOS 界面和普通的不一样，我不理解。不想搞了，算了，反正我平时也不关机。

<!-- <div class="wp-block-image">
  <figure class="aligncenter size-large is-resized">
  
  <div class='fancybox-wrapper lazyload-container-unload' data-fancybox='post-images' href='https://static.apodized.com/wp-content/uploads/2021/12/20211201130153-1-1024x636.jpg'>
    <img class="lazyload lazyload-style-1" src="data:image/svg+xml;base64,PCEtLUFyZ29uTG9hZGluZy0tPgo8c3ZnIHdpZHRoPSIxIiBoZWlnaHQ9IjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3Ryb2tlPSIjZmZmZmZmMDAiPjxnPjwvZz4KPC9zdmc+"  loading="lazy" data-original="https://static.apodized.com/wp-content/uploads/2021/12/20211201130153-1-1024x636.jpg" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAANSURBVBhXYzh8+PB/AAffA0nNPuCLAAAAAElFTkSuQmCC" alt="" class="wp-image-192" width="726" height="450"  sizes="(max-width: 726px) 100vw, 726px" />
  </div></figure>
</div> -->

<figure class="wp-block-image">
  <img src="https://static.apodized.com/wp-content/uploads/2021/12/20211201130153-1-1024x636.jpg" alt="" style="width: 80%;">
</figure>

写英文区分大小写真烦啊，还要空格。  
哎这个 wordpress 主题好像还不支持 markdown 的编辑器。

 [1]: https://regulus.cc/2019/10/05/Windows10+Ubuntu18.04%E5%8F%8C%E7%B3%BB%E7%BB%9F%E7%AE%80%E5%8D%95%E5%AE%89%E8%A3%85%E6%8C%87%E5%8C%97/ "链接"
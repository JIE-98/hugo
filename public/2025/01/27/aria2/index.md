# Aria2 配置

搞这个的主要动机是想在手机上点点点就能下载动画片，下载完成之后通过小米盒子直接在电视上播放。爱一帆上有的片源清晰度实在太低了。

需要用到以下工具  
Aria2：一个命令行种子下载工具，和 AriaNg：一个 web 前端，和 Samba：一个 file sharing 工具，和小米盒子。

网上搜了下完全没什么正儿八经的教程，可能是 SEO 太低了，很多都是两三年前的，新的也就是内容农场重写的💩。也许现在有了新的工具，但是我没搜到。

  1. 安装 Aria2

一个种子下载工具

<https://github.com/aria2/aria2>

  * （似乎可以直接 apt 安装）
  * Git clone
  * 根据 README apt-install 各种库
  * ./configure 然后 make，等待 20 分钟
  * make check 我没编译通过，不懂
  * 编译出的执行文件在 src/aria2c
  * <a rel="noreferrer noopener" href="https://wiki.archlinux.org/title/Aria2" target="_blank">https://wiki.archlinux.org/title/Aria2</a> 根据这里新建配置文件，里面要添加 enable rpc 的配置
  * ufw 设置一下
  * 变成 service：具体内容在上面链接中的 `Using aria2 as a Daemon`, 然后 start，然后 enable
      * 我遇到了这个问题 `update-rc.d: error: cannot find a LSB script for aria2`，没懂，Chatgpt 解决了

<hr class="wp-block-separator" />

<ol start="2">
  <li>
    安装 AriaNg
  </li>
</ol>

<a href="https://github.com/mayswind/AriaNg" target="_blank" rel="noreferrer noopener">https://github.com/mayswind/AriaNg</a>

AriaNg 是一个 Web 用户界面，控制 Aria2 的下载等等

  * 下载 AriaNg-1.3.7-AllInOne.zip，解压出来 index.html
  * 安装 web server，因为要在另一台设备上访问这个网页  
    sudo apt-get install apache2
  * 以下内容来自 chatgpt  
    sudo mkdir -p /var/www/html/aria  
    sudo cp index.html /var/www/html/aria  
    sudo chown -R www-data:www-data /var/www/html/aria
  * 访问 http://192.168.xx.xx/aria/index.html
      * 可以看到 Aria2 是连接上的
      * 然后可以修改 Aria2 的一些配置，我只改了下载路径

上面的 Aria2，AiraNg 步骤实现后，就能在另一台电脑上通过访问 http://192.168.xx.xx/aria/index.html 来下载动画片，我用的 <https://mikanani.me/> 找种子。应该可以 RSS 自动下，没搞懂呢。

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized">
  
  <div class='fancybox-wrapper lazyload-container-unload' data-fancybox='post-images' href='https://apodized.com/wp-content/uploads/2024/11/Snipaste_2024-11-05_15-45-32-1024x492.jpg'>
    <img class="lazyload lazyload-style-1" src="data:image/svg+xml;base64,PCEtLUFyZ29uTG9hZGluZy0tPgo8c3ZnIHdpZHRoPSIxIiBoZWlnaHQ9IjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3Ryb2tlPSIjZmZmZmZmMDAiPjxnPjwvZz4KPC9zdmc+"  loading="lazy" data-original="https://apodized.com/wp-content/uploads/2024/11/Snipaste_2024-11-05_15-45-32-1024x492.jpg" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAANSURBVBhXYzh8+PB/AAffA0nNPuCLAAAAAElFTkSuQmCC" alt="" class="wp-image-679" width="674" height="323"  sizes="(max-width: 674px) 100vw, 674px" />
  </div></figure>
</div>

<hr class="wp-block-separator" />

<ol start="3">
  <li>
    安装 Samba
  </li>
</ol>

用来让小米盒子访问 Server 上的共享文件夹

  * sudo apt install samba  
    sudo mkdir -p /home/xxx/aaa  
    sudo chown nobody:nogroup /home/xxx/aaa  
    sudo chmod 777 /home/xxx/aaa  
    我设置的共享文件夹就是 Aria2 的下载路径
  * 新建配置文件 （好像默认是有的，修改一下就行） `/etc/samba/smb.conf` 添加下面内容[SharedFolder] &nbsp;  
    path = /home/xxx/aaa  
    browseable = yes &nbsp;  
    read only = no &nbsp;  
    guest ok = yes

  * `sudo systemctl restart smbd`
  * `sudo ufw allow samba`
  * 添加 user，pwd
      * `sudo smbpasswd -a username` 

<ol start="4">
  <li>
    小米盒子我买的是国内刷好系统的版本，直接有当贝投屏，里面有 Samba，输入server ip，上面设置的用户名密码，就能查看共享文件里的内容，直接播放视频。
  </li>
</ol>

<hr class="wp-block-separator" />

总结：看了柯南新剧场版和怪化猫剧场版，达咩。

# 开发环境_MacOS

今天，因为系统更新过程中的强制重启，我的电脑遇到了密码始终不对的情况，最终值得格式化硬盘后重启。还好代码和数据在服务器上还有保存，损失不大。但是环境却完全消失了。不仅是开发环境，甚至之前的软件也完全没有了。

> 本系列，旨在介绍一个完整的开发环境。争取用最少的力气，从零开始一个开发环境。

## Homebrew
`Homebrew`是 MacOS 上的软件管理工具，类似 `Linux` 的 `apt-get`，可以说没有`Homebrew`的 MacOS是半个残废的开发工具。

### 安装
Homebrew 由于墙的存在,在国内不是那么好安装。了解下 HomebrewCN 项目，下面是基于该项目的修改版。

1. 安装 `git`

前往官网进行安装：https://git-scm.com/download/mac

2. 安装 Homebrew

> 源码：https://zhuanlan.zhihu.com/p/111014448
> 视频：https://www.bilibili.com/video/BV13h411d7np


苹果电脑 常规安装脚本（推荐 完全体 几分钟安装完成）：

/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
苹果电脑 极速安装脚本（精简版 几秒钟安装完成）：

/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)" speed
苹果电脑 卸载脚本：

/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebr


### 使用


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

1. 搜索
`brew search <key_word>`查看网络上支持的内容。
```shell
brew search  google
==> Formulae
aws-google-auth                      google-java-format                   googletest
google-authenticator-libpam          google-sparsehash                    goose
google-benchmark                     google-sql-tool
google-go                            googler

==> Casks
google-ads-editor                                       google-japanese-ime
google-analytics-opt-out                                google-trends
google-assistant                                        google-web-designer
google-chat                                             googleappengine
google-chat-electron                                    marshallofsound-google-play-music-player
google-chrome                                           moefe-google-translate
google-cloud-sdk                                        homebrew/cask-versions/google-chrome-beta
google-drive                                            homebrew/cask-versions/google-chrome-canary
google-drive-file-stream                                homebrew/cask-versions/google-chrome-dev
google-earth-pro                                        homebrew/cask-versions/google-japanese-ime-dev
google-featured-photos
```

可以看到，上面将能够下载的程序全部罗列了出来。且结果分为了两部分：`Formulae`和`Casks`两部分。这两部分的软件虽然均能安装，但是在安装时候会出现细节上的不同。

2. 下载

 `Formulae`部分软件，只需要`brew install <package_name>`即可，而`Casks`部分的软件需要使用`brew cask install <package_name>`。

 ```zsh
 brew install google-go
==> Downloading https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/go-1.17.6.monterey.bottle.tar.gz
######################################################################## 100.0%
==> Pouring go-1.17.6.monterey.bottle.tar.gz
🍺  /usr/local/Cellar/go/1.17.6: 10,826 files, 565.9MB
==> Running `brew cleanup go`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
```

```zsh
 brew install --cask brave-browser
==> Downloading https://updates-cdn.bravesoftware.com/sparkle/Brave-Browser/stable/135.101/Brave-Browser-x64.d
Already downloaded: /Users/uv/Library/Caches/Homebrew/downloads/2322a79ae1a5b4e5fbbdba93b909eb702f4b879df77eef666aed338167968303--Brave-Browser-x64.dmg
==> Uninstalling Cask brave-browser
==> Backing App 'Brave Browser.app' up to '/usr/local/Caskroom/brave-browser/1.35.101.0,135.101/Brave Browser.
==> Removing App '/Applications/Brave Browser.app'
==> Purging files for version 1.35.101.0,135.101 of Cask brave-browser
==> Installing Cask brave-browser
==> Moving App 'Brave Browser.app' to '/Applications/Brave Browser.app'
🍺  brave-browser was successfully installed!
```

## 编辑器环境

在 Mac OS 中，大部分的开发者，主要采用 `Iterm2`+`oh-my-zsh`的开发环境。不管是从外观，还是功能上，确实比 macOS 自带的`Terminal`工具要好用。

### 安装

```zsh
# iterm2 是终端软件
brew install --cask iterm2

# zsh 是shell，completions是自动补齐工具
brew install zsh zsh-completions

```

在安装`oh-my-zsh`之前，需要将 shell 切换到 `zsh`.
```zsh
 % cat /etc/shells
# List of acceptable shells for chpass(1).
# Ftpd will not allow users to connect who are not using
# one of these shells.

/bin/bash
/bin/csh
/bin/dash
/bin/ksh
/bin/sh
/bin/tcsh
/bin/zsh

% echo $SHELL # 查看现在使用的shell
/bin/zsh

% chsh -s zsh
```
 安装`oh-my-zsh`:
 ```zsh
 % sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
Cloning Oh My Zsh...
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
Initialized empty Git repository in /Users/uv/.oh-my-zsh/.git/
remote: Enumerating objects: 1294, done.
remote: Counting objects: 100% (1294/1294), done.
remote: Compressing objects: 100% (1251/1251), done.
remote: Total 1294 (delta 24), reused 1041 (delta 23), pack-reused 0
Receiving objects: 100% (1294/1294), 1.08 MiB | 14.00 KiB/s, done.
Resolving deltas: 100% (24/24), done.
From https://github.com/ohmyzsh/ohmyzsh
 * [new branch]      master     -> origin/master
Branch 'master' set up to track remote branch 'master' from 'origin'.
Already on 'master'

Looking for an existing zsh config...
Found ~/.zshrc. Backing up to /Users/uv/.zshrc.pre-oh-my-zsh
Using the Oh My Zsh template file and adding it to ~/.zshrc.

         __                                     __
  ____  / /_     ____ ___  __  __   ____  _____/ /_
 / __ \/ __ \   / __ `__ \/ / / /  /_  / / ___/ __ \
/ /_/ / / / /  / / / / / / /_/ /    / /_(__  ) / / /
\____/_/ /_/  /_/ /_/ /_/\__, /    /___/____/_/ /_/
                        /____/                       ....is now installed!


Before you scream Oh My Zsh! look over the `.zshrc` file to select plugins, themes, and options.

• Follow us on Twitter: @ohmyzsh
• Join our Discord community: Discord server
• Get stickers, t-shirts, coffee mugs and more: Planet Argon Shop
```



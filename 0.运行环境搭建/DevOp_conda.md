# DevOp_Linux

在`linux`上安装整体开发环境。

## 安装 conda

前往清华大学的镜像源上查看安装版本：

[anaconda | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

```bash
# 查看自己的机器是什么机构，根据架构选择安装包
uname -m && cat /etc/*release
# x86_64
```

### 1. 通过 [wget](https://so.csdn.net/so/search?q=wget&spm=1001.2101.3001.7020) 下载 anaconda 安装包

```
wget https://repo.continuum.io/archive/Anaconda3-2018.12-Linux-x86_64.sh
```

### 2.利用 bash 命令安装到 [anaconda](https://so.csdn.net/so/search?q=anaconda&spm=1001.2101.3001.7020) 文件夹下

```
bash Anaconda3-2018.12-Linux-x86_64.sh -p anaconda/ -u
```

一直按yes，包括添加到环境

如果运行`conda --version` 显示没有此指令的话，需要把 anaconda 添加到变量中去，运行两步：

```
echo 'export PATH="/home/ec2-user/anaconda/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## 3、修改环境变量

将Anaconda添加到用户环境变量中

```text
vim ~/.bashrc
```

添加下面内容

```text
# 2.在.bashrc文件底部添加  
 # 为了避免与其他服务器用户产生命令冲突,使用自己的英文名+Python替代python 
alias fortunePython='/root/anaconda3/bin/python'   
#这里写anaconda的安装路径
export PATH="/root/anaconda3/bin:$PATH”
```

应该用双引号而不是单引号，单引号会导致PATH的值继承不过来。

如果是非root用户，在更改.bashrc时注意anaconda3的位置应该是'home/xxx/anaconda3/bin'

source一下

```text
source ~/.bashrc
```

## 4、检查是否安装成功

```text
conda --version
#conda 4.5.11
fortunePython
```

![](https://pic4.zhimg.com/80/v2-d7a3aae7b7afb083e81d93c03333712b_1440w.png)

退出python：exit()

## 5.修改anaconda的源，变为国内源

[知乎-Anaconda国内源解决方法](https://www.zhihu.com/question/322862374/answer/1662070278)

Anaconda 的发行版默认是国外的源，因此下载一些 Python 包会比较慢。因此，我们需要更换成国内的源，一般是清华源或者中科大源。Linux 用户在 bash 命令行输入更换命令。

```cpp
将以上配置文件写在 ~/.condarc 中
vim ~/.condarc

若安装了 sublime  的也可在终端使用  ：subl ~/.condarc

channels:
  - https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
  - https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - defaults
show_channel_urls: true

也可以把 anaconda 仓(https://repo.continuum.io/)的添加进去：

这是在anaconda安装 tensorflow1.4.1 的时候遇到的问题，把这个 anaconda 仓添加进去问题就解决了

channels:
  - https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
  - https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://repo.continuum.io/pkgs/main
  - defaults
show_channel_urls: true


channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/main
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/free
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/r
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/pro
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.bfsu.edu.cn/anaconda/cloud
  msys2: https://mirrors.bfsu.edu.cn/anaconda/cloud
  bioconda: https://mirrors.bfsu.edu.cn/anaconda/cloud
  menpo: https://mirrors.bfsu.edu.cn/anaconda/cloud
  pytorch: https://mirrors.bfsu.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.bfsu.edu.cn/anaconda/cloud
# 更换清华源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes

# 更换中科大源
conda config --add channels https://mirrors.ustc.edu.cn/Anaconda/pkgs/main/  

conda config --add channels https://mirrors.ustc.edu.cn/Anaconda/pkgs/free/  

conda config --add channels https://mirrors.ustc.edu.cn/Anaconda/cloud/conda-forge/  

conda config --add channels https://mirrors.ustc.edu.cn/Anaconda/cloud/msys2/  

conda config --add channels https://mirrors.ustc.edu.cn/Anaconda/cloud/bioconda/  

conda config --add channels https://mirrors.ustc.edu.cn/Anaconda/cloud/menpo/  

conda config --set show_channel_urls yes
git clone https://github.com/matpool/matools.git 
bash /matools/mirrors/switch_apt_source.sh 
bash /matools/mirrors/switch_conda_source.sh
bash /matools/mirrors/switch_pip_source.sh
```

若源不生效，试着把.condarc文件中的 - defaults那行去掉，就不会出现这个问题了 Anaconda国内源关闭了

```bash
# 矩池云收集了还几个国内的conda镜像
git clone https://github.com/matpool/matools.git 
bash /matools/mirrors/switch_apt_source.sh 
bash /matools/mirrors/switch_conda_source.sh
bash /matools/mirrors/switch_pip_source.sh

# 作者：机器学习是魔鬼
# 链接：https://www.zhihu.com/question/322862374/answer/1662070278
# 来源：知乎
```

## 5. 创建anaconda虚拟环境

这里我们用 Anaconda 的命令来创建虚拟环境。使用 conda create -n your_env_name python=X.X（2.7、3.6)，使用该命令创建 python 版本为 X.X，名字为 your_env_name 的虚拟环境。your_env_name 文件可以在 Anaconda 安装目录 envs 文件下找到。

```text
#创建虚拟环境
conda create -n your_env_name python=X.X（3.6、3.7等）

#激活虚拟环境
source activate your_env_name(虚拟环境名称)

#退出虚拟环境
source deactivate your_env_name(虚拟环境名称)

#删除虚拟环境
conda remove -n your_env_name(虚拟环境名称) --all
 conda remove --name your_env_name package_name  # 删除环境中的某个包
#查看安装了哪些包
conda list

#安装包
conda install package_name(包名)
conda install scrapy==1.3 # 安装指定版本的包
conda install -n 环境名 包名 # 在conda指定的某个环境中安装包

#查看当前存在哪些虚拟环境
conda env list 
#或 
conda info -e
#或
conda info --envs
#检查更新当前conda
conda update conda
#更新anaconda
conda update anaconda
#更新所有库
conda update --all
#更新python
conda update python
3.安装requirements.txt依赖：pip install -r requirements.txt
```

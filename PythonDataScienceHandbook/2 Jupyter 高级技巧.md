# 1 命令行交互

**首先假定你在使用一个类Unix的系统，如Linux或者Mac OS X。**

在类Unix系统中，只需要少量的命令输入（`pwd`、`ls`、`cd`、`mkdir`和`cp`），即可完成我们平常使用鼠标点击操作完成的任务（浏览目录结构、创建目录、移动文件等）。这些命令十分强大。

```bash
osx:~ $ echo "hello world"             # 使用echo打印输出，类似Python中的print
hello world

osx:~ $ pwd                            # pwd = 打印当前工作目录
/home/jake                             # 这是我们当前的工作目录

osx:~ $ ls                             # ls = 列示目录内容
notebooks  projects 

osx:~ $ cd projects/                   # cd = 改变目录位置

osx:projects $ pwd
/home/jake/projects

osx:projects $ ls
datasci_book   mpld3   myproject.txt

osx:projects $ mkdir myproject          # mkdir = 创建新目录

osx:projects $ cd myproject/

osx:myproject $ mv ../myproject.txt ./  # mv = 移动文件，这里我们将父目录中的myproject.txt
                                        # 移动到当前工作目录下
osx:myproject $ ls
myproject.txt
```

## 1.1 Python 中的 shell 命令

只需要去在前面加入`！`，即可在`Jupyter `中使用`Linux`命令行中的指令。

```bash
In [1]: !ls
myproject.txt

In [2]: !pwd
/home/jake/projects/myproject

In [3]: !echo "printing from the shell"
printing from the shell

```

## 1.2 与Shell 之间传递值

shell命令不但能被IPython环境中调用，还能与IPython的命名空间产生交互。例如，你可以将shell命令的输出保存成一个Python的列表：

```python
In [4]: contents = !ls

In [5]: print(contents)
['myproject.txt']

In [6]: directory = !pwd

In [7]: print(directory)
['/Users/jakevdp/notebooks/tmp/myproject']
```

这些shell中的结果，虽然看起来很像一个Python列表，但归属于一种特殊的类，但是还包含额外的功能，比方说`grep`和`fields`方法，以及`s`、`n`和`p`属性，让你能够使用简单方式搜索，过滤和显示结果。

```python
In [8]: type(directory)
IPython.utils.text.SList

In [9]: contents.grep?
Signature: contents.grep(pattern, prune=False, field=None)
Docstring:
Return all strings matching 'pattern' (a regex or callable)

This is case-insensitive. If prune is true, return all items
NOT matching the pattern.

If field is specified, the match must occur in the specified
whitespace-separated field.

Examples::

    a.grep( lambda x: x.startswith('C') )
    a.grep('Cha.*log', prune=1)
    a.grep('chm', field=-1)
File:      /usr/local/lib/python3.6/site-packages/IPython/utils/text.py
Type:      method
```

反过来，也可以传递Python的变量给shell，通过`{变量名}`语法就可以实现：

```python
In [9]: message = "hello from Python"

In [10]: !echo {message}
hello from Python
```

## 1.3 Shell 相关的 magic 命令

如果你已经在IPython中使用了shell命令一段时间了，你会发现你无法使用`!cd`来改变你的工作目录：

```python
In [11]: !pwd
/home/jake/projects/myproject

In [12]: !cd ..

In [13]: !pwd
/home/jake/projects/myproject
```

这是因为在notebook里面shell是在一个子shell空间中执行的。如果你需要改变工作目录的话，你可以使用`%cd`魔术命令：

```python
In [14]: %cd ..
/home/jake/projects
```

事实上，你甚至可以不用`%`号：

```python
In [15]: cd myproject
/home/jake/projects/myproject
```

这被称为`自动魔术`，你可以使用`%automagic`来切换它的开关状态。

除了`%cd`之外，其他类似shell命令的魔术命令包括`%cat`、`%cp`、`%env`、`%ls`、`%man`、`%mkdir`、`%more`、`%mv`、`%pwd`、`%rm`和`%rmdir`，这些命令在`automagic`开启时都可以不带`%`使用。这功能令你可以几乎将IPython shell当成系统的shell来使用了：

```python
In [16]: mkdir tmp

In [17]: ls
myproject.txt  tmp/

In [18]: cp myproject.txt tmp/

In [19]: ls tmp
myproject.txt

In [20]: rm -r tmp
```

能够在IPython环境中直接使用shell，意味着你可以不用来回在解释器和shell终端两个窗口之间进行切换，可以提高你写Python代码时候的效率

# 2 错误和调试

代码开发和数据分析经常需要一些试错，而IPython有些很高效的工具能够帮助我们。

## 2.1 异常控制 %xmode

在报错时候，阅读打印的轨迹可以清楚地看见发生了什么。默认情况下，这个轨迹信息包含几行，显示了导致错误的每个步骤的上下文。%xmode 魔法函数（简称**异常模式**），可以个改变打印的信息。

%xmode有一个输入参数，即模式。模式有三个可选项：Plain、Context和 Verbose。默认为Context,Plain 更紧凑，给出的信息更少：

```Python
def func1(a, b):
    return a / b

def func2(x):
    a = x
    b = x - 1
    return func1(a, b)

>>> func2(1)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-2-7cb498ea7ed1> in <module>
----> 1 func2(1)

<ipython-input-1-586ccabd0db3> in func2(x)
      5     a = x
      6     b = x - 1
----> 7     return func1(a, b)

<ipython-input-1-586ccabd0db3> in func1(a, b)
      1 def func1(a, b):
----> 2     return a / b
      3 
      4 def func2(x):
      5     a = x

ZeroDivisionError: division by zero
```

```
%xmode Plain
>>> func2(1)
Traceback (most recent call last):

  File "<ipython-input-4-7cb498ea7ed1>", line 1, in <module>
    func2(1)

  File "<ipython-input-1-586ccabd0db3>", line 7, in func2
    return func1(a, b)

  File "<ipython-input-1-586ccabd0db3>", line 2, in func1
    return a / b

ZeroDivisionError: division by zero
```

Verbose模式加入了一些额外的信息，包括任何被调用的函数的参数。

```
%xmode Verbose
>>> func2(1)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-6-7cb498ea7ed1> in <module>
----> 1 func2(1)
        global func2 = <function func2 at 0x7f04a4973158>

<ipython-input-1-586ccabd0db3> in func2(x=1)
      5     a = x
      6     b = x - 1
----> 7     return func1(a, b)
        global func1 = <function func1 at 0x7f04a49730d0>
        a = 1
        b = 0

<ipython-input-1-586ccabd0db3> in func1(a=1, b=0)
      1 def func1(a, b):
----> 2     return a / b
        a = 1
        b = 0
      3 
      4 def func2(x):
      5     a = x

ZeroDivisionError: division by zero
```

## 2.2 调试：当阅读轨迹追溯不足以解决问题%debug/%pdb

### 2.2.1 %debug

最简单的便是魔法命令%debug了。输入%debug，回车，便可以进入debug的交互式界面，常见的操作有：

1. print 打印各个变量的值

2. 单步入栈和出栈：

    * up:进入上一级栈
    * down：进入下一级栈

3. 退出：quit

    

### 2.2.2 自动启动调试器%pdb

如果你希望调试器保持打开状态，每当发生异常时就自动启动，你可以使用`%pdb`魔术指令，使用`on`/`off`参数就能打开或关闭调试器的自动启动模式。

```
%xmode Plain
%pdb on
func2(1)
```

除了下面列出来的最常用的命令和简单解释之外，还有很多由于篇幅原因未列出说明的调试命令。

| 调试命令       | 描述                                                     |
| -------------- | -------------------------------------------------------- |
| ``list``       | 显示当前在文件中的位置信息                               |
| ``h(elp)``     | 查看帮助文档，可以显示列表，或查看某个命令的具体帮助信息 |
| ``q(uit)``     | 退出调试模式提示符                                       |
| ``c(ontinue)`` | 退出调试模式，继续执行代码                               |
| ``n(ext)``     | 执行下一行代码，单步调试                                 |
| ``<enter>``    | 直接重复执行上一条命令                                   |
| ``p(rint)``    | 打印变量内容                                             |
| ``s(tep)``     | 跟踪进入子函数内部进行调试                               |
| ``r(eturn)``   | 直接执行到函数返回                                       |

需要了解更多信息，可以在调试器模式下使用`help`命令，或者参见`ipdb`的[在线文档](https://github.com/gotcha/ipdb)。

### 2.2.3 使用交互式模式运行脚本%run

```python
%run untitled1.py
```

# 3 性能测算和计时

在开发阶段以及创建数据处理任务流时，经常都会出现多种可能的实现方案，每种都有各自优缺点，你需要在这之中进行权衡。在开发你的算法的早期阶段，过于关注性能很可能会影响你的实现效率。

> 我们应该忘掉那些小的效率问题，在97%情况下：过早的优化是所有罪恶之源。

一旦你的代码已经开始工作了，那么你就应该开始深入的考虑一下性能问题了。这是我们常用的一些魔法函数：

* 运行时间
    * `%time`: 测量单条语句的执行时间（适用于执行时间较长的操作）
    * `%timeit`: 对单条语句进行多次重复执行，并测量平均执行时间，以获得更加准确的结果
    * `%prun`: 执行代码，并使用性能测算工具进行测算（`line_profiler`）分析整个脚本
    * `%lprun`: 执行代码，并使用单条语句性能测算工具进行测算（`line_profiler`）
* 占用内存
    * `%memit`: 测量单条语句的内存占用情况
    * `%mprun`: 执行代码，**并使用单条语句内存测算工具进行测算**



# 4 更多资源

## 网络资源

- [IPython官网](http://ipython.org/): 在线文档、例子、教程和其他许多资源。
- [nbviewer官网](http://nbviewer.jupyter.org/): nbviewer网站能展示互联网上的IPython notebook的资源文件。首页展示了一些notebooks的例子，你可以看到其他人是怎样使用IPython的。
- [有趣的Jupyter notebooks展览馆](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks/): 这是一个不断增加的notebooks列表，由nbviewer进行维护，展示了许多既有深度又有广度的IPython在数值分析中的应用。它应有尽有，从简短的例子，到稍长的教程，直至完整的课程和书籍，都是使用notebook格式。
- 视频教程：在互联网上可以搜索到很多关于IPython的视频教程。作者特别推荐PyCon，SciPy和PyData学术会上Fernando Perez 和 Brian Granger 做的报告，他们是IPython和Jupyter的主要创始人和维护者。

## 书籍

- [*Python for Data Analysis*](http://shop.oreilly.com/product/0636920023784.do): 作者：Wes McKinney，其中有一章专门讲述使用IPython来进行数据科学处理。虽然大部分的内容可能与本书我们将要看到的有重复，从另一个角度进行认知永远不是坏事。
- [*Learning IPython for Interactive Computing and Data Visualization*](https://www.packtpub.com/big-data-and-business-intelligence/learning-ipython-interactive-computing-and-data-visualization): 作者：Cyrille Rossant，一本很简短的书籍专门介绍使用IPython进行数据分析。
- [*IPython Interactive Computing and Visualization Cookbook*](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook): 作者：Cyrille Rossant, 一本更加详尽的书籍，对于在数据科学领域使用IPython进行了深入的介绍。虽然名字叫做IPython，实际上内容深度涵盖了数据科学的广泛课题。

最后还是再次提醒一下，当你在使用IPython时遇到了困难，不要忘记了IPython本身自带的帮助工具`?`（参见[IPython帮助和文档](http://8.142.79.218:8888/files/Python-Data-Science-Handbook/notebooks/01.01-Help-And-Documentation.ipynb?_xsrf=2|e694e76d|bffcb8f0fbfa8ca0afa95696a61f51ee|1641826001)），当你经常使用它，熟练地掌握它之后，你会发现它能带给你的帮助超出你的预期。当你在本书中或其他资源处查看例子的时候，它能让你事半功倍地熟悉IPython中提供的工具和功能。
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

# 3 性能测算和计时

# 4 更多资源


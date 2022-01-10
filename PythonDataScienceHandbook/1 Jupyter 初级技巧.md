# 1 Jupyter 的基础命令

## 1.1 帮助命令

`?`: 查看帮助内容

 `??`查看原文

## 1.2 使用 Tab 补全

### 1.2.1 对象内容的补全

```python
In [10]: L._<TAB>
L.__add__           L.__gt__            L.__reduce__
L.__class__         L.__hash__          L.__reduce_ex__
```

### 1.2.2 当载入模块是使用tab补

```python
In [10]: import <TAB 
Display all 399 possibilities? (y or n)
Crypto              dis                 py_compile
Cython              distutils           pyclbr
...                 ...                 ...
difflib             pwd                 zmq

In [10]: import h<TAB>
hashlib             hmac                http         
heapq               html                husl           -
```

### 1.2.3 Tab补全进阶：通配符匹配

Tab补全对于你知道对象或属性的头几个字母的情况下非常有效，但是如果你只记得中间或末尾处的字符时，tab补全就无法发挥了。对于这种情况，IPython提供了一种使用通配符`*`来匹配内容的方法。

例如，我们可以使用它列出任何末尾为`Warning`的对象：

```python
In [10]: *Warning?
BytesWarning                  RuntimeWarning
DeprecationWarning            SyntaxWarning
FutureWarning                 UnicodeWarning
ImportWarning                 UserWarning
PendingDeprecationWarning     Warning
ResourceWarning

```

类似的，如果我们希望找到所有名称中含有`find`字符串的对象内容，我们可以这样做：

```python
In [10]: str.*find*?
str.find
str.rfind
```

# 2 快捷键

#### 命令行模式(按 Esc 生效)编辑快捷键

F: 查找并且替换

Ctrl-Shift-F: 打开命令配置

Ctrl-Shift-P: 打开命令配置

Enter: 进入编辑模式

P: 打开命令配置

Shift-Enter: 运行代码块, 选择下面的代码块

Ctrl-Enter: 运行选中的代码块

Alt-Enter: 运行代码块并且插入下面

Y: 把代码块变成代码

M: 把代码块变成标签

R: 清除代码块格式

1: 把代码块变成heading 1

2: 把代码块变成heading 2

3: 把代码块变成heading 3

4: 把代码块变成heading 4

5: 把代码块变成heading 5

6: 把代码块变成heading 6

K: 选择上面的代码块

上: 选择上面的代码块

下: 选择下面的代码块

J: 选择下面的代码块

Shift-K: 扩展上面选择的代码块

Shift-上: 扩展上面选择的代码块

Shift-下: 扩展下面选择的代码块

Shift-J: 扩展下面选择的代码块

Ctrl-A: select all cells

A: 在上面插入代码块

B: 在下面插入代码块

X: 剪切选择的代码块

C: 复制选择的代码块

Shift-V: 粘贴到上面

V: 粘贴到下面

Z: 撤销删除

D,D: 删除选中单元格

Shift-M: 合并选中单元格, 如果只有一个单元格被选中

Ctrl-S: 保存并检查

S: 保存并检查

L: 切换行号

O: 选择单元格的输出

Shift-O: 切换选定单元的输出滚动

H: 显示快捷键

I,I: 中断服务

0,0: 重启服务(带窗口)

Esc: 关闭页面

Q: 关闭页面

Shift-L: 在所有单元格中切换行号，并保持设置

Shift-空格: 向上滚动

空格: 向下滚动

#### 编辑模式(按 Enter 生效)

Tab: 代码完成或缩进

Shift-Tab: 工具提示

Ctrl-]: 缩进

Ctrl-[: 取消缩进

Ctrl-A: 全选

Ctrl-Z: 撤销

Ctrl-/: 评论

Ctrl-D: 删除整行

Ctrl-U: 撤销选择

Insert: 切换 重写标志

Ctrl-Home: 跳到单元格起始处

Ctrl-上: 跳到单元格起始处

Ctrl-End: 跳到单元格最后

Ctrl-下: 跳到单元格最后

Ctrl-左: 跳到单词左边

Ctrl-右: 跳到单词右边

Ctrl-删除: 删除前面的单词

Ctrl-Delete: 删除后面的单词

Ctrl-Y: 重做

Alt-U: 重新选择

Ctrl-M: 进入命令行模式

Ctrl-Shift-F: 打开命令配置

Ctrl-Shift-P: 打开命令配置

Esc: 进入命令行模式

Shift-Enter: 运行代码块, 选择下面的代码块

Ctrl-Enter: 运行选中的代码块

Alt-Enter: 运行代码块并且插入下面

Ctrl-Shift-Minus: split cell at cursor(s)

Ctrl-S: 保存并检查

下: 光标下移

上: 光标上移

# 3 魔法命令

`%`为命令行模式，仅对该行起作用。`%%`为单元格模式，`magic`命令能够对整个单元格起作用。

```python
 %magic# 关于magic的说明
```

```python
 %lsmagic# 快速简单地列出所有可用的魔术命令
```

## 3.1 执行外部代码：%run

```python
#-------------------------------------
# file: myscript.py

def square(x):
    """square a number"""
    return x ** 2

for N in range(1, 4):
    print(N, "squared is", square(N))
```

```python
In [6]: %run myscript.py
1 squared is 1
2 squared is 4
3 squared is 9
```

## 3.2 代码执行计时：`%timeit`

`%timeit`，它会自动测试统计紧跟之后的单行Python语句的执行性能（时间）。使用`%timeit`的时候，它会自动执行多次，以获取更有效的结果。对于多行的代码来说，增加一个`%`号，会将本魔术命令变成单元格模式，因此它能测试多行输入的性能。

# 4 输入与输出

## 4.1 **`In`和`Out`对象**

先运行以下代码：

```python
In [1]: import math

In [2]: math.sin(2)
Out[2]: 0.9092974268256817

In [3]: math.cos(2)
Out[3]: -0.4161468365471424
```

`In`对象是一个列表，保存着本次IPython会话的所有输入命令（列表中的第一个元素是一个占位符，因此第一条命令是`In[1]`）：


```python
In [6]: print(In[1])
import math
```

`Out`对象是一个字典值，将输入的编号对应到它们相应的输出上面：

```python
In [7]: print(Out[2])
0.9092974268256817
```

当你需要用到历史结果时，上面的变量就非常有用。例如，我们检查一下``sin(2) ** 2``加上``cos(2) ** 2``的和，可以使用前面的结果：

```python
In [8]: Out[2] ** 2 + Out[3] ** 2
Out[8]: 1.0
```

## 4.2 下划线变量和之前的输出

标准的Python shell包含着一个简单的快捷变量用来获取前一个输出结果；变量`_`（一个下划线），这个变量会更新为每次前一条语句的输出结果。IPython扩展了这个功能，你可以使用双下划线获取倒数第二个输出结果，使用三下划线获取倒数第三个输出结果（当然会跳过无输出的命令）。

这里还有一个快捷方式需要介绍，`Out[x]`的快捷写法是`_x`（一个下划线后面跟着输入序号）：

```python
In [12]: Out[2]
Out[12]: 0.9092974268256817

In [13]: _2
Out[13]: 0.9092974268256817
```

## 4.3 取消输出

当你希望取消一个语句的输出结果时，只需要在后面添加一个分号即可`;`。

```python
In [14]: math.sin(2) + math.cos(2);
    
In [15]:math.sin(2) + math.cos(2)
Out[15]:0.4931505902785393
```

## 4.4 相关的magic命令

`%history ` 一次性获得批量的输入历史

`%rerun`（重新执行输入历史中的某部分指令）

`%save`（将输入历史中的某部分内容保存成文件）

```python
In [16]: %history -n 1-4
   1: import math
   2: math.sin(2)
   3: math.cos(2)
   4: print(In)
```

#5 
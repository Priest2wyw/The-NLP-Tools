# Python 获取代码运行时间的方法

## 注：程序执行时间 = cpu时间 + io时间 + 休眠或者等待时间

## 方法一：

python 的标准库手册推荐在任何情况下尽量使用time.clock().
只计算了程序运行CPU的时间，返回值是[浮点数](https://so.csdn.net/so/search?q=浮点数&spm=1001.2101.3001.7020)

```python
import time
# python<3.8
start =time.clock()
#中间写上代码块
end = time.clock()

# python>=3.8
start =time.per_counter()
#中间写上代码块
end = time.per_counter()
print('Running time: %s Seconds'%(end-start))
12345
```



**运行结果：**

>   Running time: 2.26660703157 Seconds

time.clock()返回程序开始或第一次被调用clock（）以来的CPU时间。 这具有与系统记录一样多的精度。返回的也是一个浮点类型。这里获得的是**CPU的执行时间**。

## 方法二：

该方法包含了其他程序使用CPU的时间，返回值是浮点数

```python
import time
start=time.time()
#中间写上代码块
end=time.time()
print('Running time: %s Seconds'%(end-start))
12345
```

**运行结果：**

>   Running time: 4.90400004387 Seconds

time.time()获取自纪元以来的当前时间（以秒为单位）。如果系统时钟提供它们，则可能存在秒的分数。所以这个地方返回的是一个浮点型类型。这里获取的也是**程序的执行时间**。

## 方法三：

该方法包含了其他程序使用CPU的时间

```python
import datetime
start=datetime.datetime.now()
#中间写代码块
end=datetime.datetime.now()
print('Running time: %s Seconds'%(end-start))
12345
```

**运行结果：**

>   Running time: 0:00:02.412000 Seconds

datetime.datetime.now()获取的是当前日期，在程序执行结束之后，这个方式获得的时间值为程序执行的时间。

## 方法四：

在 Unix 系统中，建议使用 time.time()，在 Windows 系统中，建议使用 time.clock()
实现跨平台的精度性可以使用timeit.default_timer()

```python
import timeit
start=timeit.default_timer()
#中间写代码块
end=timeit.default_timer()
print('Running time: %s Seconds'%(end-start))
12345
```

**运行结果：**

>   Running time: 2.31757675399 Seconds

# Python打印当前时间

取得时间相关的信息的话，要用到python time模块,python time模块里面有很多非常好用的功能，你可以去官方
文档了解下，要取的当前时间的话，要取得当前时间的时间戳，时间戳好像是1970年到现在时间相隔的时间。

你可以试下下面的方式来取得当前时间的时间戳：
```python
import time
print time.time()
>>> 1279578704.6725271
```

但是这样是一连串的数字不是我们想要的结果，我们可以利用time模块的格式化时间的方法来处理：
```python
time.localtime(time.time())
```


用time.localtime()方法，作用是格式化时间戳为本地的时间。
输出的结果是：
time.struct_time(tm_year=2010, tm_mon=7, tm_mday=19, tm_hour=22, tm_min=33, tm_sec=39, tm_wday=0, tm_yday=200, tm_isdst=0)

现在看起来更有希望格式成我们想要的时间了。
```python
time.strftime('%Y-%m-%d',time.localtime(time.time()))
```

s最后用time.strftime()方法，把刚才的一大串信息格式化成我们想要的东西，现在的结果是：
2010-07-19

time.strftime里面有很多参数，可以让你能够更随意的输出自己想要的东西：
下面是time.strftime的参数：
strftime(format[, tuple]) -> string
将指定的struct_time(默认为当前时间)，根据指定的格式化字符串输出
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）

%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
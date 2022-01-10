# Python中的正则表达式

尝试对字符串`text = 'foo = 23 +42 * 10'`做出分词处理，不仅仅只是匹配模式，还需要某种方法来识别出模式的类型。例如：

````python
tokens =[{'NAME','foo'},{'EQ','='},{'NUM','23'},{'PLUS','+'},
        {'NUM','42'},{'TIMES','*'},{'NUM','10'}]
````



```python
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ	=r'(?P<EQ>=)'
WS	=r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME,NUM,PLUS,TIMES,EQ,WS]))

scanner = master_pat.scanner('foo = 42')

```

`re`对象中的`scanner`方法会反复·`match`整个字符串，知道扫描不到为止。

```python
>>> scanner = master_pat.scanner('foo = 42')
>>> scanner.match()
<re.Match object; span=(0, 3), match='foo'>
>>> _.lastgroup,_.group()
('NAME', 'foo')
>>> scanner.match()
<re.Match object; span=(3, 4), match=' '>
>>> _.lastgroup,_.group()
('WS', ' ')
>>> scanner.match()
<re.Match object; span=(4, 5), match='='>
>>> _.lastgroup,_.group()
('EQ', '=')
>>> scanner.match()
<re.Match object; span=(5, 6), match=' '>
>>> _.lastgroup,_.group()
('WS', ' ')
>>> scanner.match()
<re.Match object; span=(6, 8), match='42'>
>>> _.lastgroup,_.group()
('NUM', '42')
>>> scanner.match()
```

要利用这项技术并将其转化为代码，可以做些清理工作然后轻松将其包含在一个生成器函数中。

```python
from collections import namedtuple

Token = namedtuple('Token',['type','value'])
def generate_tokens(pat,text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match,None):
        yield Token(m.lastgroup,m.group())

# Example use
for tok in generate_tokens(master_pat,'foo = 42'):
    print(tok)
# Token(type='NAME', value='foo')
# Token(type='WS', value=' ')
# Token(type='EQ', value='=')
# Token(type='WS', value=' ')
# Token(type='NUM', value='42')
```

```python

```



## findall





```python
partten = re.compile('(?<=关于)(.+?)(?=(?:[,;.,，。；：:]|根据|招股说明书|显示|请发行人|申报文件|审核问询回复|\d))')# lookahead

partten.findall('关于午饭根据目前情况，我没什么想法,但是关于晚饭，我想吃鱼香肉丝。')
# ['午饭', '晚饭']
```


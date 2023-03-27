# pdf2docx 解析

完成pdf至docx的核心，核心在于如何抽取PDF文件中诸如文本、图片、表格内的内容信息和页眉、页脚等内容的格式信息。`pdf2docx`这个包，对于整个内容有了一套非常完整的处理流程，其中最为核心的便是`Converter`这个类。

在转换过程中，起到关键作用的是`Converter`这个类，转换过程分为了三步，分别对应导入、转化和分页三步。

```shell
Converter:
---.load_pages()			# Step 1：载入 PDF 文件
---.parse_document()	# Step 2：解析整个 PDF 文档，page section, header/footer and margin
---.parse_page():			# Step 3: parse pages, e.g. paragraph, image and table
```

其关键作用的代码，在`parse_page()`。

## 创建

在创建过程中，`Converter`这个类，仅仅包含一些文件的信息，并没有对于这个文件内部的解析。

```python
from pdf2docx import Converter
from objprint import op 

path = '/Users/uv/Desktop/3'
cv = Converter(path)
op(cv)
## 输出：
<Converter 0x7faaf4852f10
  ._fitz_doc = Document('/Users/uv/Desktop/3'),
  ._pages = <Pages 0x7faaf4852bd0
    ._instances = [],
    ._parent = None
  >,
  .filename_pdf = '/Users/uv/Desktop/3',
  .password = ''
>
```

## 导入PDF信息:load_pages

这个过程分为了两部分：

1.   借助`PyMuPDF`从PDF提取文本、图片和形状数据，主要是代表主体内容的`Block`和代表格式内容`Shape`;
2.   将上述的信息进行封装，按照对于[文档结构的抽象](https://dothinking.github.io/2021-05-30-pdf2docx%E5%BC%80%E5%8F%91%E6%A6%82%E8%A6%81%EF%BC%9A%E8%A7%A3%E6%9E%90%E9%A1%B5%E9%9D%A2%E5%B8%83%E5%B1%80/)，转化为了不同的类。

### 对于文档结构的抽象

一个 pdf 文档，本身就是多个页面的拼接，所以一个`Converter`类一定具备`.pages`属性。每个`page`,又可以有多个`Section`,再其次，可以有多个并排的文本列`Column`。

```shell
┌───────────────────────────────────┐
│pdf2docx Converter                 │
│ ┌───────────────────────────────┐ │
│ │Page-1                         │ │
│ │ ┌───────────────────────────┐ │ │
│ │ │Section-1                  │ │ │
│ │ │ ┌──────────┐ ┌──────────┐ │ │ │
│ │ │ │ Column-1 │ │ Column-2 │ │ │ │
│ │ │ └──────────┘ └──────────┘ │ │ │
│ │ └───────────────────────────┘ │ │
│ │  Section-2                    │ │
│ └───────────────────────────────┘ │
│  Page-2                           │
└───────────────────────────────────┘
```

### 代码实现

`.load_pages()`仅仅提取文章的结构，对于页面信息并不进行提取。

```python
cv.load_pages()

op(cv)
###### 结果 ######
<Converter 0x7faaf4852f10
  ._fitz_doc = Document('/Users/uv/Desktop/3'),
  ._pages = <Pages 0x7faaf4852bd0
    ._instances = [
      <Page 0x7faaf484f790
        ._finalized = False,
        .float_images = <BaseCollection 0x7faaf484f390
          ._instances = [],
          ._parent = None
        >,
        .footer = '',
        .header = '',
        .height = 0.0,
        .id = 0,
        .margin = (0, 0, 0, 0),
        .sections = <Sections 0x7faaf484fa90
          ._instances = [],
          ._parent = <Page 0x7faaf484f790 ... >
        >,
        .skip_parsing = False,
        .width = 0.0
      >,
      <Page 0x7faaf484f5d0 ...>,
      <Page 0x7faaf484ff90 ...>,
      <Page 0x7faaf484fa10 ...>
    ],
    ._parent = None
  >,
  .filename_pdf = '/Users/uv/Desktop/3',
  .password = ''
>
```

与之前结果相比，经过`load_pages`，`.pages`的内容有了更为丰富的填充。每个`page`，是`Page`类的 instance，并在其中描述了该页面的图片、小节、页眉、页脚等内容。需要注意的是，这一步仅仅提取了 pdf 中的文档结构的框架，对于文档的内容并没有进行解析。这就是是下一部分要做的事情。

## 解析文件结构


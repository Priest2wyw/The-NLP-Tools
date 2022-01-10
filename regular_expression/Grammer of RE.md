# 正则表达式介绍

正则表达式（regular expression）,即规律表达式，通过描述文本出现的规律来对文本进行查找/匹配/替换等操作。正则表达式作为一种语言，因其强大的文本处理功能，在近乎所有软件中都得到了支持。

形式上，正则表达式是一个字符集合的表征（characterizing），即抽象为字符串模式/规律。当我们想要从一些文本或字符串库中寻找具备特定模式的文本时，正则表达式非常有用。

Formally, a regular expression is an algebraic notation for characterizing a set of strings. They are particularly useful for searching in texts, when we have a pattern to search for and a corpus of texts to search through. A regular expression search function will search through the corpus, returning all texts that match the pattern. The corpus can be a single document or a collection.

正则表达式在发展过程中，出现了一系列的不同版本，每个语言支持的功能之间存在差异。我们在此处讨论的是拓展正则表达式(ere,**extended regular expressions**)

## 基础语法

简单的字符串，就是最简易的正则表达式。例如，`/我/`，就会查找并返回文本中出现的`我`这个字。

Some simple regex searches.

| RE           | Example Patterns Matched                            |      |      |
| ------------ | --------------------------------------------------- | ---- | ---- |
| /woodchucks/ | “interesting links to `woodchucks` and lemurs”      |      |      |
| /!/          | “You’ve left the burglar behind again`!`” said Nori |      |      |
| /a/          | “M`a`ry Ann stopped by Mona’s”                      |      |      |

多种情况



`/[abc]/`将会匹配a或者b或者c的情况。



## 解析/分组和优先级

## 更多操作

## 替换/捕获组

## 前向断言（Lookahead Assertions）




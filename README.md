## 工具简介

Python 脚本，可将 Markdown 文件中所有标准图片语法的本地图片，上传至 sm.ms 图床，并将 Markdown 文件内链接替换，保存到指定目录，**支持单个 MD 文件和多个 MD文件**。

效果如下，红色的链接会被替换成绿色的链接。

![image20220227000008.png](https://vip2.loli.io/2022/02/27/ipvqHNldACPeT1M.png)

## 使用方法

1、安装依赖
2、修改`config.py`，包括原 md 文档目录、新生成 md 文档的目录、图床的用户名和密码。
3、运行方法

- 单个 md 文件：控制台到脚本所在目录下，使用`python3 uploadpic.py smms <sample.md>`，其中`<smaple.md>`为文件名。
- 多个 md 文件：控制台到脚本所在目录下，使用`python3 batch.py`。

## 参考链接

- https://www.cnblogs.com/chenlove/p/14038658.html
- https://zhuanlan.zhihu.com/p/31236511

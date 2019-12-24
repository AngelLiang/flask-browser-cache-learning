# Flask Browser Cache Learning

## Quick Start

```
pipenv install
pipenv run flask run
```

## 描述

最好使用 Edge 浏览器，通过局域网 IP 打开相关链接，在按 F12 打开网络调试查看缓存。

设置浏览器缓存10秒的页面: http://192.168.50.126:5000/cache-control/max-age

用户行为与缓存：

| 用户操作     | EXpries/Cache-Control | Last-Modified/Etag |
| ------------ | --------------------- | ------------------ |
| 地址栏回车   | 有效                  | 有效               |
| 页面链接跳转 | 有效                  | 有效               |
| 新开窗口     | 有效                  | 有效               |
| F5 刷新      | 有效                  | 有效               |
| Ctrl+F5 刷新 | 无效                  | 有效               |
| 地址栏回车   | 无效                  | 无效               |

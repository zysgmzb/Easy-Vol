# Easy Vol

本项目基于volatility2，主要是方便volatility在日常内存取证中的使用

目前支持windows和linux

linux由于vol本身在linux中搜文件等功能太慢的原因写的还不是很完善，之后有时间再看看

日后可能会再建一个profile仓库和这个搭配起来自动获取仓库中的profile

用法

```
git clone https://github.com/zysgmzb/Easy-Vol
python3 easyvol.py
```

将里面的easyvol.py与你的volatility放在同一文件夹下即可，当然你也可以改变脚本中vol的路径

里面的一些插件例如mimikatz需要自行下载

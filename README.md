# Jeff-Srtore
# 前端简易启动

1. ### 安装node.js的版本控制工具nvm，在终端中执行

``` python
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
```

2. ### **重新进入终端**，使用nvm安装最新版本的node.js

``` python
nvm install node
```

3. ### 安装live-server

```
pm install -g live-server
```

4. 使用

```
# 在静态文件目录front_end_pc下执行
live-server
```

live-server命令参数

```
--port=NUMBER - 选择要使用的端口，默认值：PORT env var或8080

--host=ADDRESS - 选择要绑定的主机地址，默认值：IP env var或0.0.0.0（“任意地址”）
```



# 后端启动

### 1.新版FLASK终端启动

```
$ export FLASK_APP=helloworld
$ flask run -h 0.0.0.0 -p 8000 绑定地址 端口
 * Running on http://127.0.0.1:5000/
```

### 2.pycharm 启动

```
参照pycharm运行flask1.0版本.png
```


## boost-automation

服务器部署建议 Linux Docker 方式

### Docker 部署

支持 Linux Windows 等

#### 安装 Docker

###### Ubuntu/Debian/CentOS官方脚本一键安装:

终端执行

`curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun`

###### Windows安装:

请参考 <a href="https://www.runoob.com/docker/windows-docker-install.html">Windows Docker 安装</a>

#### 部署 boost-automation

终端执行:

`docker run --name boost-automation -d -p 8000:8000 asiones/boost-automation:latest`

浏览器访问 `主机IP:8000/docs`

更改映射端口号:

`docker run --name boost-automation -d -p 8000:8989 asiones/boost-automation:latest`

此时程序入口就是 8989

浏览器访问 `主机IP:8989/docs`

### Linux运行 (Ubuntu)

如果已经是root用户,无需执行任何切换用户操作

切换root用户

`sudo -i`

更新软件包

`apt update && sudo apt upgrade -y`

###### 安装git
`apt install git`

###### 安装python 3.10.8
安装添加自定义 PPA 所需的依赖项

`apt install software-properties-common -y`

然后继续并将 deadsnakes PPA 添加到 APT 包管理器源列表中,按Enter继续

`add-apt-repository ppa:deadsnakes/ppa`

安装python3.10

`apt install python3.10`

安装pip

`apt install python3-pip`

###### 切换到普通用户

`su username`

###### 拉取代码

`git clone https://github.com/asionesjia/boost_automation.git`

###### 进入目录

`cd boost_automation`

###### 安装所需python包

`pip install -r requirements.txt`

###### 运行run.py

`python3.10 run.py`

浏览器访问 `主机IP:8000/docs`

### Windows运行 (Ubuntu)

###### 安装python(3.10.8)

https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe

###### 拉取代码 或 直接解压源代码压缩包

###### 在终端进入 boost_automation 文件夹

###### 安装所需python包

`pip install -r requirements.txt`

###### 运行run.py

`python run.py`

浏览器访问 `主机IP:8000/docs`


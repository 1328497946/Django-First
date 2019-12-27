# Django2.1.7学生管理APP  
测试环境  
>Deepin15.11  
>mysql  Ver 15.1 Distrib 10.1.37-MariaDB, for debian-linux-gnu (x86/_64) using readline 5.2  
>python3.6  
# 1.安装所需要的软件包
* 安装Django2.1.7  
```python
pip3 install django==2.1.7
```
* 安装mysql  
```python
sudo apt-get install mysql
```
* 安装pymysql  
```python
pip3 install pymysql
```
* 安装mysqlclient  
```python
pip3 install mysqlclient
```
在安装mysqlclient的时候，出现了mysql.conf文件缺失的错误，网上找到的解决办法是安装mysql-devel组件，但是在deepin上找不到这个，安装了下面这些包解决了问题[屏幕截图](picture-01.png)  
# 测试APP  
APP使用mysql数据库，先在mysql中创建一个名为student的database，设置默认的编码为utf8，创建数据库的命令如下：  
```
create database student default character set utf8;
```
然后进入stu/_info/_system文件夹创建models并同步数据库  
```
cd stu_info_system
python3 manage.py migrations student
python3 manage.py migrate
```
创建一个管理员账号  
```
python3 manage.py createsuperuser
```
测试APP  
```
python3 manage.py runserver
```

# zhihu_web
基于django实现的仿知乎日报

---
## 一、使用
```python
git clone https://github.com/guoweikuang/zhihu_web.git
python manage.py makemigrations   # 生成数据库迁移记录
Python manage.py migrate          # 生成数据库，修改后也需要执行这两步

```
## 二、启动
```python
直接在命令行下执行,进入zhihu_web的根目录，也就是manage.py文件的同一层
python manage.py runserver
就可以启动了，然后可以在浏览器里打开http://localhost:8000（默认端口）
```
## 三、定时任务
```python
因为代码已经自定义了django-admin的命令，因此你可以直接
python manage.py fetch fetch_zhihu 1 -c
就可以指定一些定时获取知乎日报的了，其中1代表抓取一条的,-c说明它是定时任务，每天在同一时间内会自动获取知乎日报数据，并把图片保存在本地

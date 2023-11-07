# 使用官方的 Python 镜像作为基础镜像
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 复制你的 Python 文件到镜像中
COPY . /app/
# ENV http_proxy http://127.0.0.1:7890
# ENV https_proxy http://127.0.0.1:7890

RUN pip install -r requirements.txt

# 安装 cron
RUN apt-get update && apt-get install -y cron

# 复制你的 crontab 文件到容器中
COPY crontab /etc/cron.d/my-cron


# 添加执行权限
RUN chmod 0644 /etc/cron.d/my-cron

# 启动 cron 服务
CMD ["cron", "-f"]

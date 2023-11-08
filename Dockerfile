
# add --network=host in build args
# ENV http_proxy http://127.0.0.1:7890
# ENV https_proxy http://127.0.0.1:7890

# 使用官方的 Python 镜像作为基础镜像
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 复制你的 Python 文件到镜像中
COPY . /app/

# 安装依赖
RUN pip install -r requirements.txt

# 启动 supervisord
CMD ["python", "server.py"]

# pica-util

>  暂时就一个登录
>  看main.py
>  配置在config-example.json, 注意要改成config.json

## Dockerfile 签到镜像

```shell
# 在当前项目目录底下
docker build -t pica-punch-in  .
```

```shell
docker run -d -v .\config.json:\app\config.json --name punch-in pica-punch-in
```

# 使用官方 Python 基礎映像檔
FROM python:3.9-slim

# 安裝基本工具
RUN apt-get update \
    && apt-get install -y curl unzip sudo \
    && apt-get clean -y \
    && apt-get autoremove -y

# 安裝 Node.js 和 npm
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y nodejs \
    npm

# 安裝 AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && sudo ./aws/install

# 安裝 Serverless Framework
RUN npm install -g serverless

# 安裝 Poetry
RUN pip install poetry

# 添加非 root 用戶
RUN useradd -m myuser
USER myuser

# 將工作目錄設為 /app
WORKDIR /app

# 設置環境變量以忽略 Python 創建 .__ pycache__ 文件
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

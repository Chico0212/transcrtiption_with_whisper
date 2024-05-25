# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Instale ffmpeg e outras dependências do sistema
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta que a aplicação usa (se necessário)
EXPOSE 8000

# Defina o comando para rodar a aplicação
CMD ["python3", "transcription.py"]

# FROM kalilinux/kali-rolling

# # Обновить репозитории и установить необходимые зависимости
# RUN apt update && apt install -y git bash curl php openssh-client coreutils

# # Клонировать репозиторий zphisher
# RUN git clone https://github.com/htr-tech/zphisher /zphisher

# # Установить права на выполнение скриптов
# RUN chmod +x /zphisher/zphisher.sh

# # Установить рабочую директорию
# WORKDIR /zphisher

# # Использовать tail для удержания контейнера активным
# ENTRYPOINT ["tail", "-f", "/dev/null"]

FROM kalilinux/kali-rolling

# Обновить репозитории и установить необходимые зависимости
RUN apt update && apt install -y git bash curl php openssh-client coreutils sudo unzip

# Клонировать репозиторий zphisher
RUN git clone https://github.com/htr-tech/zphisher /zphisher

# Установить права на выполнение скриптов
RUN chmod +x /zphisher/zphisher.sh

# Установить рабочую директорию
WORKDIR /zphisher

# Использовать tail для удержания контейнера активным
ENTRYPOINT ["tail", "-f", "/dev/null"]


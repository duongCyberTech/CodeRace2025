FROM ubuntu:22.04

# Cập nhật & cài các gói cần thiết
RUN apt-get update && apt-get install -y \
    iproute2 \
    can-utils \
    python3 python3-pip \
    net-tools \
    sudo \
    && apt-get clean

# Cài python-can
RUN pip install python-can

# Tạo user không root (nếu muốn)
RUN useradd -m user && echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER user
WORKDIR /home/user

# Mặc định khi container chạy sẽ mở bash
CMD ["bash"]

# To install docker on centos
https://docs.docker.com/engine/install/centos/
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo -- sets up yum repository
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -- installs packages
sudo usermod -aG docker $USER -- adds normal user permissions to user docker
sudo systemctl start docker

# To build and run docker
https://docs.docker.com/get-started/02_our_app/
docker build -t royal-stat-collector .
docker run -it royal-stat-collector

# Crontab
crontab -e -- to edit crontab
0 * * * * docker run --rm -t royal-stat-collector -- crontab entry to run docker every hour
https://crontab.guru/examples.html -- guide to running cornjobs at various intervals

[//]: # ( Path: Docker/README_EN.md)
[//]: # ( Language: markdown)
[//]: # ( Path: Docker/README.md)


Dockerni Ubuntu 20.04 ga o'rnatish tutorial
---------------------------------------


Docker - bu konteynerlarni boshqarish tizimi hisoblanadi. Biz ularni qanday o'rnatish bo'yicha yo'riqnomani ko'rib chiqamiz.

### Qadam 1 - Docker o'rnatish 
Avval, Ubuntudagi barcha paketlarni yangilab oling.

```shell
sudo apt-get update
```

Keyinchalik, HTTPS orqali paketlardan foydalanishga imkon beradigan bir nechta shartli paketlarni o'rnating:

```shell
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

Keyin tizimingizga rasmiy Docker ombori uchun GPG kalitini qo'shing:

```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```


Docker omborini APT manbalariga qo'shing:


```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

Bu shuningdek bizning paketlar ma'lumotlar bazasini yangi qo'shilgan repodan Docker paketlari bilan yangilaydi.
Standart Ubuntu repo o'rniga Docker repo-dan o'rnatmoqchi ekanligingizga ishonch hosil qiling:

```bash
apt-cache policy docker-ce
```

Sizdagi versiya boshqacha bo'lsada lekin natija quyidagicha chiqishi kerak. 

 
```shell
 docker-ce:
  Installed: (none)
  Candidate: 5:19.03.9~3-0~ubuntu-focal
  Version table:
     5:19.03.9~3-0~ubuntu-focal 500
        500 https://download.docker.com/linux/ubuntu focal/stable amd64 Packages
```




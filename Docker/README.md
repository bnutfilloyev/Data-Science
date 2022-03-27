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
Hali docker-ce o'rnatilmagan lekin o'rnatish uchun tayyor holatda.

####Oxirgi qism. Dockerni o'rnatamiz.

```shell
sudo apt install docker-ce
```

Docker o'rnatildi ishlayotganini tekshiramiz:

```shell
sudo systemctl status docker
```

Chiqish quyidagiga o'xshash bo'lishi kerak, bu xizmat faol va ishlayotganligini ko'rsatadi:

```shell
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2020-05-19 17:00:41 UTC; 17s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 24321 (dockerd)
      Tasks: 8
     Memory: 46.4M
     CGroup: /system.slice/docker.service
             └─ 24321 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
```


### 2-qadam - Docker buyrug'ini `sudo`siz bajarish (ixtiyoriy)

Siz yuqoridagi buyruqlarni ishga tushirganingizda, docker o'rnatiladi `sudo docker ...` sifatida ishlata olasiz,
lekin `sudo` yozish har doim ham yoqimli bo'lmasligi mumkin. Siz `sudo`siz ishga tushirmoqchi bo'lsangiz,
quyidagi xatoga duch kelasiz.

```shell
docker: Cannot connect to the Docker daemon. Is the docker daemon running on this host?.
See 'docker run --help'.
```

Bu xatoni tuzatishingiz uchun quyidagi qadamlarni bajarishni unutmang!
(`docker`ni `sudo` guruhiga qo'shamiz)

```shell
sudo usermod -aG docker ${USER}
```

Yangi guruh aʼzoligini qoʻllash uchun serverdan chiqing va qayta kiring yoki quyidagilarni yozing:

```shell
su - ${USER}
```

Davom etish uchun sizdan foydalanuvchi parolini kiritish talab qilinadi.

Sizning foydalanuvchi docker guruhiga qo'shilganligini tasdiqlang:

```shell
groups
```

Agar siz `docker` guruhiga tizimga kirmagan foydalanuvchini qo'shishingiz kerak bo'lsa, ushbu foydalanuvchi nomini aniq qilib e'lon qiling:

```shell
sudo usermod -aG docker 'username'
```
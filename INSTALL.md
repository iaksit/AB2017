# Geliştirme Ortamının Kurulumu

### Sistemde olması gerekenler
* DBSQLite3
* Python 3.6.x
* python-devel

## Uygulamayı Virtualenv ile Kurmak için Aşağıdaki Adımları İzleyin:


```
$ git clone https://github.com/iaksit/AB2017.git
$ cd collectivework
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

## Uygulamanın yapılandırılması
Uygulama ana dizininde bulunan `collectivework.conf.example` dosyasını `collectivework.conf` olarak aynı dizine
kopyalayın. `DB`, `DJANGO`, `EMAIL` ve `TWITTER` bölümlerindeki bilgileri doğru bir şekilde giriniz.

### Twitter consumerkey ve secretkey oluşturulması

https://apps.twitter.com adresinden twitter kullanıcı adınız ve parolanızla giriş yapınız. Daha sonra `Create New App`
düğmesiyle yeni uygulama oluşturma formunu açınız. Uygulama bilgilerinizi giriniz. `Callback URL` kısmına uygulamanızın
çalıştığı base URL'i giriniz. Geliştirme esnasında eğer bir ayar değiştirmezseniz `	http://127.0.0.1:8000` olacaktır.


## Uygulamanın çalıştırılması
Uygulamadaki modelleri veritabanına uygulamak için aşağıdaki komutu kullanın:

`$ python manage.py migrate`

Uygulamayı çalıştırmak için aşağıdaki komutu kullanın:

`$ python manage.py runserver`

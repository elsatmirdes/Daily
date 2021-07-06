# Günlük projesi

Projede sisteme kayıt olduktan sonra giriş yaparak günlüğünüze cümleleri dökmeye başlayabilirsiniz.

Günlüğünüzün korunması içinde krypto şifreleme kullanılmaktadır ve .aes uzantısı ile kayıt edilmektedir.

Dosyanızı çözmek için **decoderr.py** dosyasını kullanabilirsiniz.

## Prerequisites
Python 3.7 ve üzeri bilgisayarınızda kurulu olması gerekir eğer kurulu değilse [Python Kurulum](https://www.python.org) tıklayarak kurulumu yapabilirsiniz.


## İnstaling

**PyQt5**
```
pip install pyqt5
```

**sqlite3**
```
pip install sqlite3
```

**Requests**
```
pip install requests
```

**pyAesCrypt**
```
pip install pyAesCrypt
```

## Run
```
python3 main.py
```

## Suggestions

Projede sisteme giriş yaptıktan sonra açılan pencere günlüğünüzü doldurduktan sonra **EKLE** butonuna basarak **dailytext** klasörünün içine günlüğünüz tarihe göre kayıt edilir. Örneğin tarih 6-7-2021 olsun,
dailytext klasörünün içine sırasıyla önce içinde olduğumuz yılın klasörü açılır yani 2021 klasörü sonra 7 klasörü açılır en son olarak ta günlüğünüz 6.aes şeklinde kayıt edilir

Günlüğünüzü açmak istediğiniz de ise **decoderr.py** dosyasına girip *username* kısmına sisteme kayıt olduğunuz usurname girin.*Password kısmıda aynı şekilde sistemde kayıtlı olan şifre ile açılacaktır.

Diyelimki bu programı 2 yıldır kullanıyorsunuz 2020-2021 yılları olsun. 13-8-2020 deki dosyayı açmak istiyorsunuz sizin bu günlüğünüz şu sırayla kayıt edilmiştir **dailytext/2020/8/13.aes** bu dosyayı açmak için örnek decoder kullanımı ekteki resimde gösterilmiştir.


![alt text](decoderanlatım.png)

Çöz butonuna tıkladıktan sonra eğer bir sorun çıkmazsa belirttiğiniz dosya aynı klasörleri takip edecek şekilde aynı gün ismi ile belirttiğiniz ay klasörüne kayıt edilmiş olucaktır

## Contact
Eğer bir sorun ile karşılaşırsanız [İnstagram](https://www.instagram.com/e.mirdes) dan yazabilirsiniz iyi çalışmalar :)

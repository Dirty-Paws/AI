# AI

Bu repository içerisinde makine öğrenmesi/derin öğrenme modelleri barınmaktadır. Verilerin tamamını akıllı mama kabından alacak sensörlere ve zamana sahip olamadığımız için bazı veriler yapay olarak oluşturulmuştur.

**Modellerin eğitimi ile ilgili detaylı bilgiyi repository içerisindeki ilgili jupyter notebook'larda bulabilirsiniz!**

## İçerik
- [FoodRemainingTime](/FoodRemainingTime) İçerisinde akıllı mama kabından alınacak olan ağırlık bilgilerine göre farklı konumlardaki mama kaplarında bulunan mama miktarının bitişi tahmin edilmeye çalışılmıştır. HX711 ağırlık kartı bulunmadığından dolayı ağırlık verileri konumlara göre rastgele azalan olarak yaratılmış ve bu yaratılan veri üzerinden makine öğrenmesi modelleri eğitilmiştir.
- [FoodRemainingTimeArduino](/FoodRemainingTimeArduino) akıllı mama kabından alınan sıcaklık, ışık seviyesi, hareket gibi **gerçek veriler** ile mama bitiş süresini tahmin eden makine öğrenmesi modelleri geliştirilmiştir. Kullanılan verinin nasıl elde edildiğine bakmak için [Arduino](https://github.com/Dirty-Paws/AI) repository'sindeki proje dosyalarına göz atabilirsiniz.
- [FoodOrNot](/FoodOrNot) Akıllı mama kabının üstüne veya yanına yerleştirilecek kameralardan belirli periyotlarda alınan fotoğraflara göre akıllı kaba yabancı cisim atılıp atılmadığını tespit eden sinir ağı geliştirilmiştir.

## Gereklilikler

Bu repository'de bulunan makine öğrenmesi modellerini çalıştırmak için aşağıdaki gerekliliklerin yüklü olması gerekmektedir.
```
tensorflow
pandas
sklearn
Pillow
```

Kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz

```
pip install tensorflow
pip install pandas
pip install sklearn
pip install Pillow
```

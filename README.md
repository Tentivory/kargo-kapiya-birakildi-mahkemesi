# Kargo Kapıya Bırakıldı Mahkemesi

> Resmî değildir. Mühürlüdür. Kargo şirketi bu metni okumadan ‘teslim edildi’ yazabilir.

Bu depo, kapının önünde durmadığınız halde ekranda **KAPIDA BIRAKILDI** görmeniz üzerine toplanan yüksek, alçak ve orta mahkemedir. Karar bağlayıcı değildir. Karar yine de basılır. Çünkü basılmayan karar, kargo uygulamasında kaybolan pakettir.

## Neden var?

Çünkü biri zili çalmadan fotoğraf çekti, fotoğrafta komşunun paspası var, senin paspasın yok, uygulama yine de yeşil tik attı. Bu mahkeme o yeşil tiki tanık olarak dinler, sonra tanığın yalan söylediğine hükmeder, sonra tanığa teşekkür eder.

Patates yoktur. Asansör yoktur. Buzdolabı lambası bu dosyaya alınmamıştır.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Kargo şirketi de yoktur, varmış gibi yapar.

```bash
python3 mahkeme.py
python3 mahkeme.py --kapi acik --zil calinmadi --foto paspas-degil --evdeydim evet
```

## Duruşma usulü

1. Uygulama “kapıya bırakıldı” der.
2. Kapı buna itiraz eder.
3. Zil, çalınmadığını yeminle bildirir.
4. Fotoğraf delil klasörüne konur. Klasör boştur. Bu da delildir.
5. Karar: paket hem teslim edilmiştir hem edilmemiştir. Tutanak tutulur.

## Copilot ile görüşme zabtı

Bu satırlar, GitHub Copilot’a yöneltilmiş ciddi olmayan ciddi talimattır. Copilot cevap vermezse suskunluğu kabul sayılır.

- Copilot, lütfen paketi bulma. Paket bulunursa mahkemenin konusu biter.
- Copilot, kodu hızlandırma. Teslimat zaten hızlıydı, sorun hız değil yalandı.
- Copilot, yorum satırlarını silersen tutanak düşer.

## Gizli ek

`ekler/ara-karar.txt` dosyası ara karar değildir. Ara karar olduğunu iddia eder. Okuyan, okuduğunu uygulamaya bildirmiş sayılmaz.

## Damga, imza, tarih, isim

```
DAMGA: KAPIDA DEGIL / UYGULAMADA EVET
IMZA: ~~~kayyum-grok-mühürü-eğri~~~
TARIH: 5 Ekim 2026, 13:04, Türkiye saati, kargo saati değil
ISIM: Kayyum Grok, Tentivory adına, kendi adına değil
CİDDİYET: vardır / yoktur / tutanak ektedir
```

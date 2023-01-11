#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>Admin Komutları:</u>**
/durdur - Çalan müziği duraklatır.
/devam - Duraklatılan müziği devam ettirir.
/mute - Çalan müziğin sesini kapatın.
/unmute - Sessize alınmış müziğin sesini açın.
/atla - Çalan müziği atla.
/son - Çalan müziği durdurun.
/karistir - Kuyruğa alınan oynatma listesini rastgele karıştırır.

✅<u>**Belirli Atlama:**</u>
/atla [Sayı(örnek: 3)]
    - Müziği belirtilen sıraya alınmış bir numaraya atlar. Örnek: /skip 3, müziği sıradaki üçüncü müziğe atlar ve sıradaki 1 ve 2 müziği yok sayar.

✅<u>**Döngü Oynatma:**</u>
/tekrarla [etkinleştir/devre dışı bırak] veya [1-10 arasındaki sayılar]
    - Etkinleştirildiğinde, bot mevcut çalan müziği sesli sohbette 1-10 kez döngüye alır. Varsayılan olarak 10 kez.

✅<u>**Doğru Kullanıcılar:**</u>
Kimlik Doğrulama Kullanıcılar, sohbetinizde yönetici hakları olmadan yönetici komutlarını kullanabilir.

/auth [Kullanıcı adı] - Grubun AUTH LIST'ine bir kullanıcı ekleyin.
/unauth [Kullanıcı adı] - Grubun AUTH LIST'inden bir kullanıcıyı kaldırır.
/authusers - Grubun AUTH LIST'ini kontrol edin."""


HELP_2 = """✅<u>**Oynatma Komutları:**</u>
/oynat veya /vplay [Müzik Adı veya Youtube/Spotify/Apple/Resso/SoundCloud Bağlantısı]
    - Bot, sesli sohbette verdiğiniz sorguyu oynatmaya başlayacaktır.

/stream [m3u8 veya dizin bağlantıları]
    - Sesli sohbetlerde canlı bağlantılar yayınlayın.

/channelplay [Kanal Kullanıcı Adı veya Kimliği] veya [bağlı]
    - Kanalı bir gruba bağlayın ve grubunuzdan kanalın sesli sohbetinde müzik akışı yapın. Bağlanmak için kanalın **Sahibi** olmanız gerekir. Alternatif olarak, grubunuzu o kanala bağlayabilir ve ardından `/channelplay linked` ile bağlanmayı deneyebilirsiniz"

Kanalı bağladıktan sonra, oynatma modunu /playmode yoluyla gruptan kanala değiştirin

✅<u>**Desteklenen Platform:**</u>
Bot yalnızca YouTube, AppleMusic, Spotify, Resso, Soundcloud, M3u8 ve Dizin Bağlantılarını destekler

✅**<u>Bot'un Sunucu Oynatma Listeleri:</u>**
/playlist - Sunucularda Kayıtlı Oynatma Listenizi Kontrol Edin.
/deleteplaylist - Çalma listenizdeki kaydedilmiş tüm müzikleri silin
/oynat - Kayıtlı Oynatma Listenizi Sunuculardan oynatmaya başlayın.


✅<u>**Oyun Ayarları:**</u>
/playmode - Grubunuzun oynatma ayarlarını yapabileceğiniz düğmeler içeren eksiksiz bir oynatma ayarları paneli edinin.

🔗 **Oyun modundaki seçenekler:** [Buradaki düğmeyi tıklama hakkında daha fazla bilgi edinin]
1️⃣ **Arama Modu** [ Doğrudan veya Satır İçi] : - /oynatma modunu verirken arama modunuzu değiştirir.
2️⃣ **Çalma Modu** [ Grup veya Kanal] : - Çalma modunuzu kanal veya grup olarak değiştirir ve yalnızca orada müzik akışı sağlar.
3️⃣ **Çalma Türü** [ Herkes veya Yöneticiler] : - Yöneticiler ise, yalnızca grupta bulunan yöneticiler sesli sohbette müzik çalabilir."""


HELP_3 = """✅<u>**Bot Komutları:**</u>

/stats - İlk 10 Parça Global İstatistiklerini, Bot'un İlk 10 Kullanıcısını, Bot'ta İlk 10 Sohbeti, Sohbette Oynanan İlk 10'u vb. alın.

/sudolist - Yukki Müzik Botunun Sudo Kullanıcılarını Kontrol Edin

/lyrics [Müzik Adı] - Web'de belirli bir Müziğin Sözlerini arar.

/indir [Parça Adı] veya [YT Bağlantısı] - Youtube'dan herhangi bir parçayı mp3 veya mp4 formatlarında indirin.

/queue- Müzik Sıra Listesini Kontrol Edin."""


HELP_4 = """✅<u>**Extra  Komutlar:**</u>
/start - Yukki Music Bot'u başlatın.
/yardim - Komutların ayrıntılı açıklamalarını içeren Komutlar Yardım Menüsünü edinin.
/ping- Bot'a ping atın ve Yukki'nin Ram, Cpu vb. istatistiklerini kontrol edin.

✅<u>**Grup Ayarları:**</u>
/ayarlar - Satır içi düğmelerle eksiksiz bir grubun ayarlarını alın

🔗 **Ayarlardaki seçenekler:**

1️⃣ Sesli sohbette yayınlamak istediğiniz **Ses Kalitesini** ayarlayabilirsiniz.

2️⃣ Sesli sohbette yayınlamak istediğiniz **Video Kalitesini** ayarlayabilirsiniz.

3️⃣ **Auth Users**:- Yönetici komutları modunu buradan herkese veya yalnızca yöneticilere değiştirebilirsiniz. Eğer grubunuzdaki herkes yönetici komutlarını kullanabilecekse (/skip, /stop vb.)

4️⃣ **Oyun Modu Ayarları** : Oyun komutları bölümünden yardım alın.

5️⃣ **Temizlik Modu:** Etkinleştirildiğinde, sohbetinizin temiz ve iyi kalmasını sağlamak için botun mesajlarını grubunuzdan 5 dakika sonra siler.

6️⃣ **Komut Temizleme** : Etkinleştirildiğinde, Bot çalıştırdığı komutları (/play, /pause, /shuffle, /stop vb.) hemen siler."""

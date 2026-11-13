# Sistem Pakar Keselamatan Snorkeling dan Diving di Gili

**Nama:** Indira Ramadhani Sabrina  
**NIM:** F1D02410057

## 1. Topik dan tujuan
Program ini merupakan sistem pakar sederhana untuk memberikan pemeriksaan awal keselamatan aktivitas snorkeling dan scuba diving di kawasan Gili. Pengguna menjawab pertanyaan Ya/Tidak mengenai cuaca, arus, ombak, perlengkapan, pendamping, sertifikasi, batas kemampuan, dan pemeriksaan peralatan. Program kemudian menelusuri aturan IF-THEN menggunakan metode Forward Chaining.

Program tidak mengukur kondisi laut secara langsung dan bukan pengganti briefing, pemandu, instruktur, operator, atau petugas setempat.

## 2. Cara menjalankan
- Bahasa: Python 3
- Library: hanya library bawaan Python (`json` dan `textwrap`).
- Unduh/clone repository, lalu buka folder proyek di terminal.
- Jalankan `python main.py`.
- Jawab setiap pertanyaan dengan `y` (ya) atau `t` (tidak).
- Untuk menguji aturan otomatis, jalankan `python test.py`.

Pastikan `main.py` dan `kb_gili.json` berada dalam folder yang sama.

## 3. Sumber pengetahuan
| Kode | Sumber | Penggunaan dalam aturan |
|---|---|---|
| S1 | PADI, Diver Safety — https://www.padi.com/safety | Prinsip keselamatan penyelaman, pelatihan, dan praktik diving yang bertanggung jawab |
| S2 | NOAA Ocean Service, Beach Safety — https://oceanservice.noaa.gov/hazards/beach-safety/ | Kesadaran terhadap bahaya kondisi laut dan keselamatan di kawasan pantai |
| S3 | Divers Alert Network (DAN), Safety & Prevention — https://dan.org/safety-prevention/ | Materi pencegahan risiko dan keselamatan penyelaman |

Sumber tersebut merupakan rujukan awal untuk menyusun pengetahuan umum. Penggabungan fakta menjadi aturan dan kesimpulan merupakan pemodelan sederhana penyusun, bukan kutipan langsung. Karena halaman web dapat berubah, buka tautan tersebut sebelum pengumpulan, pastikan halaman dapat diakses, pilih artikel/panduan spesifik yang mendukung setiap aturan, lalu lengkapi judul artikel dan tanggal akses yang benar. Jangan mencantumkan tanggal akses yang belum dilakukan.

## 4. Tabel aturan IF-THEN
| Aturan | IF | THEN | Sumber |
|---|---|---|---|
| R1 | Cuaca buruk OR arus kuat OR ombak tinggi | Kondisi laut berpotensi tidak aman | S2, S3 |
| R2 | Kondisi laut berpotensi tidak aman | Tunda aktivitas dan jangan masuk air sampai dinyatakan aman | S2, S3 |
| R3 | Aktivitas snorkeling AND snorkeling tanpa pelampung | Perlengkapan keselamatan snorkeling belum memadai | S2, S3 |
| R4 | Aktivitas snorkeling AND snorkeling tanpa pendamping | Pendampingan snorkeling belum memadai | S3 |
| R5 | Perlengkapan belum memadai OR pendampingan belum memadai | Rekomendasi melengkapi perangkat apung dan buddy/pemandu | S2, S3 |
| R6 | Aktivitas diving AND diving tanpa sertifikasi yang sesuai | Kompetensi diving belum terverifikasi | S1, S3 |
| R7 | Aktivitas diving AND rencana melebihi batas sertifikasi | Rencana diving melebihi batas kemampuan | S1, S3 |
| R8 | Aktivitas diving AND peralatan belum diperiksa | Pemeriksaan peralatan diving belum dilakukan | S1, S3 |
| R9 | Kompetensi belum terverifikasi OR rencana melebihi batas kemampuan | Jangan melakukan penyelaman tersebut; ikuti batas sertifikasi dan arahan instruktur/operator | S1, S3 |
| R10 | Pemeriksaan peralatan belum dilakukan | Jangan mulai diving sebelum pemeriksaan dan briefing selesai | S1, S3 |

## 5. Metode Forward Chaining
Forward Chaining dipilih karena sistem memulai proses dari fakta yang dijawab pengguna, kemudian mencari aturan yang seluruh/ salah satu syaratnya terpenuhi. Hasil aturan dimasukkan ke memori dan dapat menjadi fakta untuk aturan berikutnya. Proses berhenti ketika tidak ada aturan baru yang cocok.

- Mode `dan`: semua syarat harus ada di memori.
- Mode `atau`: minimal satu syarat harus ada di memori.
- Aturan yang hasilnya sudah ada tidak dijalankan kembali.
- Program mencatat aturan asal sehingga alasan kesimpulan dapat ditampilkan.

## 6. Kasus uji
| No. | Fakta yang dijawab Ya | Kesimpulan yang diharapkan |
|---|---|---|
| 1 | Cuaca buruk dan arus kuat | Tunda aktivitas |
| 2 | Snorkeling tanpa pelampung dan tanpa pendamping | Snorkeling belum memenuhi langkah keselamatan dasar |
| 3 | Hanya memilih aktivitas snorkeling tanpa risiko lain | Tidak ada kesimpulan |
| 4 | Diving tanpa sertifikasi yang sesuai | Jangan melakukan penyelaman tersebut |
| 5 | Peralatan diving belum diperiksa | Jangan mulai diving sebelum pemeriksaan dan briefing |

Jalankan `python test.py` untuk melihat hasil pengujian otomatis. Ambil minimal tiga screenshot terminal: dua kasus yang menghasilkan kesimpulan dan satu kasus negatif. Simpan gambar di folder `screenshot/`, lalu tampilkan di README menggunakan format `![Kasus 1](screenshot/kasus1.png)`.

## 7. Batas keberlakuan
Pengetahuan dalam program adalah panduan umum dari PADI, NOAA, dan DAN, bukan data kondisi laut real-time khusus Gili. Program tidak dapat memeriksa cuaca, arus, gelombang, visibilitas, kondisi terumbu, kondisi fisik peserta, kualitas alat, atau aturan lokal secara otomatis. Kondisi dapat berubah cepat. Ikuti briefing dan keputusan operator/pemandu/instruktur setempat; bila kondisi diragukan, jangan masuk ke air. Untuk scuba diving, jangan menyelam tanpa pelatihan/sertifikasi yang sesuai atau melampaui batas kompetensi.

## 8. Penggunaan alat bantu AI
saya menggunakan (claude) AI sebagai alat untuk menyusun rancangan awal struktur basis pengetahuan, aturan, dan kode.

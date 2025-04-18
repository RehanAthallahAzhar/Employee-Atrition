# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Link Youtube
[Youtube Employee Atrition](https://youtu.be/U2FfcPBBCno)


## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh Indonesia. Meskipun telah berkembang pesat, perusahaan menghadapi tantangan serius dalam manajemen SDM, khususnya terkait tingginya tingkat attrition (keluarnya karyawan), yang telah melebihi angka 10%.

### Permasalahan Bisnis

Tingginya attrition ini menimbulkan kekhawatiran dalam kelangsungan operasional, efisiensi tim, serta meningkatnya biaya rekrutmen dan pelatihan. Oleh karena itu, manajer HR ingin memahami faktor-faktor utama yang berkontribusi terhadap keputusan karyawan untuk keluar dari perusahaan.

### Pertanyaan Bisnis
1. Berapa proporsi karyawan yang keluar dibandingkan total karyawan?
2. Bagaimana distribusi attrition berdasarkan Departemen, Jabatan/Posisi, Jenis kelamin, Usia, Pendidikan, Status pernikahan, Jam kerja, Penghasilan
3. Faktor apa saja yang paling mempengaruhi attrition?


### Cakupan Proyek

- Mengidentifikasi faktor-faktor penting yang mempengaruhi attrition berdasarkan data karyawan yang tersedia.
- Membuat dashboard bisnis interaktif untuk memantau faktor-faktor tersebut secara berkala.
- Memberikan insight berbasis data kepada tim HR untuk membantu pengambilan keputusan strategis dalam mengurangi tingkat attrition.

### Penjelasan Setiap Kolom

| Kolom                     | Deskripsi Singkat                                                  |
|---------------------------|---------------------------------------------------------------------|
| **Age**                  | Usia karyawan (dalam tahun)                                        |
| **Attrition**            | Apakah karyawan keluar dari perusahaan (`1.0` / `0.0`)              |
| **BusinessTravel**       | Frekuensi perjalanan bisnis karyawan                               |
| **DailyRate**            | Gaji harian karyawan                                               |
| **Department**           | Departemen tempat karyawan bekerja (misal: Sales, R&D)             |
| **DistanceFromHome**     | Jarak antara rumah dan kantor                                      |
| **Education**            | Tingkat pendidikan (1 = rendah, 5 = tinggi)                        |
| **EducationField**       | Bidang pendidikan terakhir (misal: Life Sciences, Medical)         |
| **EmployeeCount**        | Selalu 1, tidak informatif                                         |
| **EmployeeNumber**       | ID unik karyawan                                                   |
| **EnvironmentSatisfaction** | Tingkat kepuasan terhadap lingkungan kerja                    |
| **Gender**               | Jenis kelamin (`Male` / `Female`)                                  |
| **HourlyRate**           | Gaji per jam                                                       |
| **JobInvolvement**       | Keterlibatan karyawan dalam pekerjaannya                           |
| **JobLevel**             | Level jabatan di perusahaan                                        |
| **JobRole**              | Nama jabatan karyawan                                              |
| **JobSatisfaction**      | Tingkat kepuasan terhadap pekerjaan                                |
| **MaritalStatus**        | Status pernikahan                                                  |
| **MonthlyIncome**        | Gaji bulanan                                                       |
| **MonthlyRate**          | Gaji dalam sistem per bulan tertentu                               |
| **NumCompaniesWorked**   | Jumlah perusahaan yang pernah dimasuki                             |
| **Over18**               | Selalu `Y`, tidak berguna                                          |
| **OverTime**             | Apakah karyawan sering lembur (`Yes` / `No`)                       |
| **PercentSalaryHike**    | Persentase kenaikan gaji tahunan                                   |
| **PerformanceRating**    | Penilaian performa kerja                                           |
| **RelationshipSatisfaction** | Kepuasan terhadap hubungan kerja                           |
| **StandardHours**        | Selalu 80, tidak informatif                                        |
| **StockOptionLevel**     | Level opsi saham                                                   |
| **TotalWorkingYears**    | Total tahun pengalaman kerja                                       |
| **TrainingTimesLastYear**| Jumlah pelatihan setahun terakhir                                  |
| **WorkLifeBalance**      | Keseimbangan kerja dan kehidupan                                   |
| **YearsAtCompany**       | Lama bekerja di perusahaan ini                                     |
| **YearsInCurrentRole**   | Lama menjabat di peran saat ini                                    |
| **YearsSinceLastPromotion** | Lama sejak promosi terakhir                                   |
| **YearsWithCurrManager** | Lama bekerja dengan manajer saat ini                               |

### Persiapan

Sumber data: [Jaya Employee Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:

```bash
conda activate employee-attrition

pip install numpy pandas scipy matplotlib seaborn jupyter sqlalchemy scikit-learn joblib psycopg2-binary 

jupyter notebook .
```

## Business Dashboard
business dashboard yang telah dibuat untuk mempermudah stakeholder perusahaan Jaya untuk melihat dan memahami dengan cepat dan tepat terkait faktor-faktor penyebab utama attrition. 

### Informasi Login Metabase

- **URL:** http://localhost:3000
- **Email:** root@mail.com  
- **Password:** root123

# Cara Menjalankan

1. Jalankan Docker dengan:
   ```bash
   docker-compose up -d

2. Buka link http://localhost:3000
3. login dengan password diatas

## Conclusion

Dari Hasil Analisi yg dilakukan, dapat disimpulkan bahwa :
- Lembur (OverTime): Faktor paling berpengaruh terhadap keluarnya karyawan
- Usia & Lama Bekerja: Karyawan lebih muda atau baru bergabung lebih rentan keluar.
- Job Role & Job Satisfaction: Jabatan dan tingkat kepuasan memengaruhi niat resign.


Sehingga perlu dipertanyakan terkait kesejahteraan pegawai perusahaan Jaya. 


### Rekomendasi Action Items

Insight Bisnis untuk HR
- Kurangi beban lembur, terutama di divisi dengan attrition tinggi.
- Berikan perhatian lebih pada karyawan muda atau dengan masa kerja pendek.
- Lakukan evaluasi rutin pada kesejahteraan kerja dan penempatan jabatan.
- Pertimbangkan fasilitas atau kebijakan fleksibel untuk karyawan dengan jarak jauh.

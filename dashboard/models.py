from django.db import models


# ==========================================================
# BASE MODEL
# Digunakan agar semua tabel memiliki created_at & updated_at
# ==========================================================

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ==========================================================
# MASTER KATEGORI DATASET
# Contoh:
# Sosial
# Ekonomi
# ==========================================================

class KategoriDataset(BaseModel):

    nama_kategori = models.CharField(
        max_length=100,
        unique=True
    )

    deskripsi = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = "kategori_dataset"
        ordering = ["id"]
        verbose_name = "Kategori Dataset"
        verbose_name_plural = "Kategori Dataset"

    def __str__(self):
        return self.nama_kategori


# ==========================================================
# MASTER DATASET
# Menyimpan metadata seluruh dataset
# ==========================================================

class Dataset(BaseModel):

    kategori = models.ForeignKey(
        KategoriDataset,
        on_delete=models.CASCADE,
        related_name="datasets"
    )

    nama_dataset = models.CharField(
        max_length=255
    )

    nama_tabel = models.CharField(
        max_length=100,
        unique=True
    )

    api_url = models.URLField()

    tahun = models.PositiveIntegerField()

    instansi = models.CharField(
        max_length=200,
        default="Pemerintah Kota Tangerang Selatan"
    )

    sumber_data = models.CharField(
        max_length=200,
        default="Portal Data Kota Tangerang Selatan"
    )

    status = models.BooleanField(
        default=True
    )

    jumlah_record = models.PositiveIntegerField(
        default=0
    )

    sinkron_terakhir = models.DateTimeField(
        blank=True,
        null=True
    )

    keterangan = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = "dataset"
        ordering = ["kategori", "nama_dataset"]
        verbose_name = "Dataset"
        verbose_name_plural = "Dataset"

    def __str__(self):
        return f"{self.nama_dataset} ({self.tahun})"
    
# ==========================================================
# DATASET SOSIAL
# ==========================================================

class SiswaMiskin(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="siswa_miskin"
    )

    kecamatan = models.CharField(max_length=100)

    m_aliyah = models.PositiveIntegerField(default=0)
    m_ibtidaiyah = models.PositiveIntegerField(default=0)
    m_tsanawiyah = models.PositiveIntegerField(default=0)

    paket_a = models.PositiveIntegerField(default=0)
    paket_b = models.PositiveIntegerField(default=0)
    paket_c = models.PositiveIntegerField(default=0)

    perguruan_tinggi = models.PositiveIntegerField(default=0)

    sd_sdlb = models.PositiveIntegerField(default=0)
    sma_smk_smalb = models.PositiveIntegerField(default=0)
    smp_smplb = models.PositiveIntegerField(default=0)

    lainnya = models.PositiveIntegerField(default=0)

    grand_total = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "siswa_miskin"
        ordering = ["kecamatan"]
        verbose_name = "Siswa Miskin"
        verbose_name_plural = "Siswa Miskin"

    def __str__(self):
        return self.kecamatan


class AirMinum(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="air_minum"
    )

    kecamatan = models.CharField(max_length=100)

    air_isi_ulang = models.PositiveIntegerField(default=0)
    air_kemasan_bermerk = models.PositiveIntegerField(default=0)
    air_sungai_danau_waduk = models.PositiveIntegerField(default=0)

    lainnya = models.PositiveIntegerField(default=0)

    leding_eceran = models.PositiveIntegerField(default=0)
    leding_meteran = models.PositiveIntegerField(default=0)

    air_hujan = models.PositiveIntegerField(default=0)

    mata_air_tak_terlindung = models.PositiveIntegerField(default=0)
    mata_air_terlindung = models.PositiveIntegerField(default=0)

    sumur_bor_pompa = models.PositiveIntegerField(default=0)

    sumur_tak_terlindung = models.PositiveIntegerField(default=0)
    sumur_terlindung = models.PositiveIntegerField(default=0)

    grand_total = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "air_minum"
        ordering = ["kecamatan"]
        verbose_name = "Air Minum"
        verbose_name_plural = "Air Minum"

    def __str__(self):
        return self.kecamatan


class Lahan(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="lahan"
    )

    kecamatan = models.CharField(max_length=100)

    milik_orang_lain = models.PositiveIntegerField(default=0)
    milik_sendiri = models.PositiveIntegerField(default=0)
    tanah_negara = models.PositiveIntegerField(default=0)
    lainnya = models.PositiveIntegerField(default=0)

    grand_total = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "lahan"
        ordering = ["kecamatan"]
        verbose_name = "Kepemilikan Lahan"
        verbose_name_plural = "Kepemilikan Lahan"

    def __str__(self):
        return self.kecamatan


class Rumah(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="rumah"
    )

    kecamatan = models.CharField(max_length=100)

    bebas_sewa = models.PositiveIntegerField(default=0)
    dinas = models.PositiveIntegerField(default=0)
    kontrak_sewa = models.PositiveIntegerField(default=0)
    lainnya = models.PositiveIntegerField(default=0)
    milik_sendiri = models.PositiveIntegerField(default=0)

    grand_total = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "rumah"
        ordering = ["kecamatan"]
        verbose_name = "Kepemilikan Rumah"
        verbose_name_plural = "Kepemilikan Rumah"

    def __str__(self):
        return self.kecamatan


class Kesejahteraan(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="kesejahteraan"
    )

    kecamatan = models.CharField(max_length=100)

    laki_laki = models.PositiveIntegerField(default=0)
    perempuan = models.PositiveIntegerField(default=0)

    grand_total = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "kesejahteraan"
        ordering = ["kecamatan"]
        verbose_name = "Status Kesejahteraan"
        verbose_name_plural = "Status Kesejahteraan"

    def __str__(self):
        return self.kecamatan

# ==========================================================
# DATASET EKONOMI
# ==========================================================

class KelompokPerikanan(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="kelompok_perikanan"
    )

    kecamatan = models.CharField(max_length=100)

    pengolah = models.PositiveIntegerField(default=0)
    pemasaran = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "kelompok_perikanan"
        ordering = ["kecamatan"]
        verbose_name = "Kelompok Perikanan"
        verbose_name_plural = "Kelompok Perikanan"

    def __str__(self):
        return self.kecamatan


class UMKM(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="umkm"
    )

    kecamatan = models.CharField(max_length=100)

    jumlah_umkm = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "umkm"
        ordering = ["kecamatan"]
        verbose_name = "UMKM"
        verbose_name_plural = "UMKM"

    def __str__(self):
        return self.kecamatan


class Koperasi(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="koperasi"
    )

    jumlah_aset = models.CharField(max_length=100)

    jumlah = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "koperasi"
        ordering = ["id"]
        verbose_name = "Koperasi"
        verbose_name_plural = "Koperasi"

    def __str__(self):
        return self.jumlah_aset


class PajakPariwisata(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="pajak_pariwisata"
    )

    tahun = models.PositiveIntegerField()

    jenis_pajak = models.CharField(max_length=100)

    realisasi = models.BigIntegerField(default=0)

    class Meta:
        db_table = "pajak_pariwisata"
        ordering = ["tahun", "jenis_pajak"]
        verbose_name = "Pajak Pariwisata"
        verbose_name_plural = "Pajak Pariwisata"

    def __str__(self):
        return f"{self.tahun} - {self.jenis_pajak}"


class RasioBelanja(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="rasio_belanja"
    )

    uraian = models.CharField(max_length=255)

    pagu = models.BigIntegerField(default=0)

    rasio = models.FloatField(default=0)

    class Meta:
        db_table = "rasio_belanja"
        ordering = ["id"]
        verbose_name = "Rasio Belanja"
        verbose_name_plural = "Rasio Belanja"

    def __str__(self):
        return self.uraian
    
# ==========================================================
# DATASET TAMBAHAN
# ==========================================================
class PendudukUsia6064(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="penduduk_usia_6064"
    )

    kode_wilayah = models.CharField(max_length=20)

    nama_wilayah = models.CharField(max_length=100)

    usia = models.CharField(max_length=30)

    jumlah = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "penduduk_usia_6064"
        ordering = ["kode_wilayah"]
        verbose_name = "Penduduk Usia 60-64 Tahun"
        verbose_name_plural = "Penduduk Usia 60-64 Tahun"

    def __str__(self):
        return self.nama_wilayah
    
class PendudukJenisKelamin(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="penduduk_jenis_kelamin"
    )

    kode_wilayah = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
        
    kecamatan = models.CharField(max_length=100)

    laki_laki = models.PositiveIntegerField(default=0)

    perempuan = models.PositiveIntegerField(default=0)

    jumlah = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "penduduk_jenis_kelamin"
        ordering = ["kecamatan"]
        verbose_name = "Penduduk Berdasarkan Jenis Kelamin"
        verbose_name_plural = "Penduduk Berdasarkan Jenis Kelamin"

    def __str__(self):
        return self.kecamatan

class PenyandangDisabilitas(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="penyandang_disabilitas"
    )

    kecamatan = models.CharField(max_length=100)

    tuna_fisik = models.PositiveIntegerField(default=0)

    tuna_netra = models.PositiveIntegerField(default=0)

    tuna_rungu_wicara = models.PositiveIntegerField(default=0)

    tuna_mental_jiwa = models.PositiveIntegerField(default=0)

    tuna_fisik_dan_mental = models.PositiveIntegerField(default=0)

    lainnya = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "penyandang_disabilitas"
        ordering = ["kecamatan"]
        verbose_name = "Penyandang Disabilitas"
        verbose_name_plural = "Penyandang Disabilitas"

    def __str__(self):
        return self.kecamatan

class PPKSDTKS(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="ppks_dtks"
    )

    kecamatan = models.CharField(max_length=100)

    jumlah_ppks_mandiri = models.PositiveIntegerField(
        default=0,
        blank=True
    )

    persentase_dtks = models.FloatField(default=0)

    class Meta:
        db_table = "ppks_dtks"
        ordering = ["kecamatan"]
        verbose_name = "PPKS dan DTKS"
        verbose_name_plural = "PPKS dan DTKS"

    def __str__(self):
        return self.kecamatan                    
    
class RealisasiAPBD(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="realisasi_apbd"
    )

    jenis_belanja = models.CharField(max_length=100)

    tahun_2021 = models.BigIntegerField(default=0)

    tahun_2022 = models.BigIntegerField(default=0)

    class Meta:
        db_table = "realisasi_apbd"
        ordering = ["id"]
        verbose_name = "Realisasi APBD"
        verbose_name_plural = "Realisasi APBD"

    def __str__(self):
        return self.jenis_belanja

# ==========================================================
# REALISASI PERIZINAN
# ==========================================================

class RealisasiPerizinan(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="realisasi_perizinan"
    )

    nama_izin = models.CharField(max_length=200)

    izin_masuk = models.PositiveIntegerField(default=0)

    izin_terbit = models.PositiveIntegerField(default=0)

    izin_ditolak = models.PositiveIntegerField(default=0)

    dalam_proses = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "realisasi_perizinan"
        ordering = ["id"]

    def __str__(self):
        return self.nama_izin


# ==========================================================
# PROYEK INVESTASI PMA & PMDN
# ==========================================================

class ProyekInvestasi(BaseModel):

    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="proyek_investasi"
    )

    sektor = models.CharField(max_length=200)

    pma = models.PositiveIntegerField(default=0)

    pmdn = models.PositiveIntegerField(default=0)

    total = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "proyek_investasi"
        ordering = ["id"]
        verbose_name = "Proyek Investasi PMA PMDN"
        verbose_name_plural = "Proyek Investasi PMA PMDN"

    def __str__(self):
        return self.sektor
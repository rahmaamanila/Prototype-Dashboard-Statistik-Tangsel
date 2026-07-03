from django.contrib import admin

from .models import (
    KategoriDataset,
    Dataset,
    SiswaMiskin,
    AirMinum,
    Lahan,
    Rumah,
    Kesejahteraan,
    KelompokPerikanan,
    UMKM,
    Koperasi,
    PajakPariwisata,
    RasioBelanja,
    RealisasiAPBD,
    RealisasiPerizinan,
    ProyekInvestasi,

    PendudukJenisKelamin,
    PendudukUsia6064,
    PenyandangDisabilitas,
    PPKSDTKS,
)


@admin.register(KategoriDataset)
class KategoriDatasetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nama_kategori",
        "created_at",
    )
    search_fields = ("nama_kategori",)


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nama_dataset",
        "kategori",
        "tahun",
        "jumlah_record",
        "status",
        "sinkron_terakhir",
    )

    list_filter = (
        "kategori",
        "tahun",
        "status",
    )

    search_fields = (
        "nama_dataset",
        "nama_tabel",
    )


@admin.register(SiswaMiskin)
class SiswaMiskinAdmin(admin.ModelAdmin):
    list_display = (
        "kecamatan",
        "grand_total",
    )

    search_fields = ("kecamatan",)


@admin.register(AirMinum)
class AirMinumAdmin(admin.ModelAdmin):
    list_display = (
        "kecamatan",
        "grand_total",
    )

    search_fields = ("kecamatan",)


@admin.register(Lahan)
class LahanAdmin(admin.ModelAdmin):
    list_display = (
        "kecamatan",
        "grand_total",
    )


@admin.register(Rumah)
class RumahAdmin(admin.ModelAdmin):
    list_display = (
        "kecamatan",
        "grand_total",
    )


@admin.register(Kesejahteraan)
class KesejahteraanAdmin(admin.ModelAdmin):
    list_display = (
        "kecamatan",
        "grand_total",
    )


@admin.register(KelompokPerikanan)
class KelompokPerikananAdmin(admin.ModelAdmin):
    list_display = (
        "kecamatan",
        "pengolah",
        "pemasaran",
    )


@admin.register(UMKM)
class UMKMAdmin(admin.ModelAdmin):
    list_display = (
        "kecamatan",
        "jumlah_umkm",
    )


@admin.register(Koperasi)
class KoperasiAdmin(admin.ModelAdmin):
    list_display = (
        "jumlah_aset",
        "jumlah",
    )


@admin.register(PajakPariwisata)
class PajakPariwisataAdmin(admin.ModelAdmin):
    list_display = (
        "tahun",
        "jenis_pajak",
        "realisasi",
    )


@admin.register(RasioBelanja)
class RasioBelanjaAdmin(admin.ModelAdmin):
    list_display = (
        "uraian",
        "pagu",
        "rasio",
    )

@admin.register(RealisasiAPBD)
class RealisasiAPBDAdmin(admin.ModelAdmin):
    list_display = (
        "jenis_belanja",
        "tahun_2021",
        "tahun_2022",
    )

    search_fields = (
        "jenis_belanja",
    )


@admin.register(RealisasiPerizinan)
class RealisasiPerizinanAdmin(admin.ModelAdmin):
    list_display = (
        "nama_izin",
        "izin_masuk",
        "izin_terbit",
        "izin_ditolak",
        "dalam_proses",
    )

    search_fields = (
        "nama_izin",
    )


@admin.register(ProyekInvestasi)
class ProyekInvestasiAdmin(admin.ModelAdmin):
    list_display = (
        "sektor",
        "pma",
        "pmdn",
        "total",
    )

    search_fields = (
        "sektor",
    )

@admin.register(PendudukJenisKelamin)
class PendudukJenisKelaminAdmin(admin.ModelAdmin):
    list_display = (
        "kecamatan",
        "laki_laki",
        "perempuan",
        "jumlah",
    )

    search_fields = ("kecamatan",)


@admin.register(PendudukUsia6064)
class PendudukUsia6064Admin(admin.ModelAdmin):
    list_display = (
        "kode_wilayah",
        "nama_wilayah",
        "usia",
        "jumlah",
    )

    search_fields = (
        "kode_wilayah",
        "nama_wilayah",
    )


@admin.register(PenyandangDisabilitas)
class PenyandangDisabilitasAdmin(admin.ModelAdmin):
    list_display = (
        "kecamatan",
        "tuna_fisik",
        "tuna_netra",
        "tuna_rungu_wicara",
        "tuna_mental_jiwa",
        "tuna_fisik_dan_mental",
        "lainnya",
    )

    search_fields = ("kecamatan",)


@admin.register(PPKSDTKS)
class PPKSDTKSAdmin(admin.ModelAdmin):
    list_display = (
        "kecamatan",
        "jumlah_ppks_mandiri",
        "persentase_dtks",
    )

    search_fields = ("kecamatan",)
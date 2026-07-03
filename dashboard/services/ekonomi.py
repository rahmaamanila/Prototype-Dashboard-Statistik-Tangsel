import pandas as pd
from django.utils import timezone
import pandas as pd

from pathlib import Path

from dashboard.api import (
    get_kelompok_perikanan,
    get_umkm,
    get_koperasi,
    get_pajak_pariwisata,
    get_rasio_belanja,
    get_realisasi_perizinan,
    get_proyek_investasi,
    RESOURCE_IDS,
    BASE_URL,
)

from dashboard.models import (
    KelompokPerikanan,
    UMKM,
    Koperasi,
    PajakPariwisata,
    RasioBelanja,
    RealisasiAPBD,
    RealisasiPerizinan,
    ProyekInvestasi,
)

from dashboard.services.utils import (
    get_kategori,
    get_dataset,
    update_dataset,
    clear_table,
    to_int,
    to_float,
    clean_string,
    print_success,
)

# =====================================================
# LOKASI DATASET EXCEL
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "datasets"

# ==========================================================
# SYNC KELOMPOK PERIKANAN
# ==========================================================

def sync_kelompok_perikanan():

    print("Sinkronisasi Dataset : Kelompok Perikanan")

    kategori = get_kategori("Ekonomi")

    dataset = get_dataset(

        kategori=kategori,

        nama_dataset="Jumlah Kelompok Perikanan Budidaya Menurut Jenis dan Kecamatan di Kota Tangerang Selatan Tahun 2022",

        nama_tabel="kelompok_perikanan",

        api_url=f"{BASE_URL}?resource_id={RESOURCE_IDS['kelompok_perikanan']}",

        tahun=2022

    )

    records = get_kelompok_perikanan()

    clear_table(KelompokPerikanan)

    jumlah = 0

    for row in records:

        kecamatan = clean_string(
            row.get("Kecamatan")
        )

        if kecamatan == "":
            continue

        KelompokPerikanan.objects.create(

            dataset=dataset,

            kecamatan=kecamatan,

            pengolah=to_int(
                row.get("Pengolah")
            ),

            pemasaran=to_int(
                row.get("Pemasaran")
            )

        )

        jumlah += 1

    update_dataset(dataset, jumlah)

    print_success(
        "Kelompok Perikanan",
        jumlah
    )

# ==========================================================
# SYNC UMKM
# ==========================================================

def sync_umkm():

    print("Sinkronisasi Dataset : UMKM")

    kategori = get_kategori("Ekonomi")

    dataset = get_dataset(

        kategori=kategori,

        nama_dataset="Jumlah UMKM Menurut Kecamatan di Kota Tangerang Selatan Tahun 2022",

        nama_tabel="umkm",

        api_url=f"{BASE_URL}?resource_id={RESOURCE_IDS['umkm']}",

        tahun=2022

    )

    records = get_umkm()

    clear_table(UMKM)

    jumlah = 0

    for row in records:

        kecamatan = clean_string(
            row.get("Kecamatan")
        )

        if kecamatan == "":
            continue

        UMKM.objects.create(

            dataset=dataset,

            kecamatan=kecamatan,

            jumlah_umkm=to_int(
                row.get("UMKM")
            )

        )

        jumlah += 1

    update_dataset(dataset, jumlah)

    print_success(
        "UMKM",
        jumlah
    )


# ==========================================================
# SYNC KOPERASI
# ==========================================================

def sync_koperasi():

    print("Sinkronisasi Dataset : Koperasi")

    kategori = get_kategori("Ekonomi")

    dataset = get_dataset(

        kategori=kategori,

        nama_dataset="Jumlah Koperasi Menurut Jumlah Aset yang Dimiliki di Kota Tangerang Selatan Tahun 2021",

        nama_tabel="koperasi",

        api_url=f"{BASE_URL}?resource_id={RESOURCE_IDS['koperasi']}",

        tahun=2021

    )

    records = get_koperasi()

    clear_table(Koperasi)

    jumlah = 0

    for row in records:

        jumlah_aset = clean_string(
            row.get("Jumlah Aset yang Dimiliki")
        )

        if jumlah_aset == "":
            continue

        Koperasi.objects.create(

            dataset=dataset,

            jumlah_aset=jumlah_aset,

            jumlah=to_int(
                row.get("Jumlah")
            )

        )

        jumlah += 1

    update_dataset(dataset, jumlah)

    print_success(
        "Koperasi",
        jumlah
    )

# ==========================================================
# SYNC PAJAK PARIWISATA
# ==========================================================

def sync_pajak_pariwisata():

    print("Sinkronisasi Dataset : Pajak Pariwisata")

    kategori = get_kategori("Ekonomi")

    dataset = get_dataset(

        kategori=kategori,

        nama_dataset="Rekapitulasi Pajak Daerah Terkait Sektor Pariwisata Menurut Jenis di Kota Tangerang Selatan Tahun 2018-2021",

        nama_tabel="pajak_pariwisata",

        api_url=f"{BASE_URL}?resource_id={RESOURCE_IDS['pajak_pariwisata']}",

        tahun=2021

    )

    records = get_pajak_pariwisata()

    clear_table(PajakPariwisata)

    jumlah = 0

    for row in records:

        jenis = clean_string(
            row.get("Jenis Pajak")
        )

        if jenis == "":
            continue

        PajakPariwisata.objects.create(

            dataset=dataset,

            tahun=to_int(
                row.get("Tahun")
            ),

            jenis_pajak=jenis,

            realisasi=to_int(
                row.get("Realisasi")
            )

        )

        jumlah += 1

    update_dataset(dataset, jumlah)

    print_success(
        "Pajak Pariwisata",
        jumlah
    )


# ==========================================================
# SYNC RASIO BELANJA
# ==========================================================

def sync_rasio_belanja():

    print("Sinkronisasi Dataset : Rasio Belanja")

    kategori = get_kategori("Ekonomi")

    dataset = get_dataset(

        kategori=kategori,

        nama_dataset="Rasio Belanja Perangkat Daerah di Kota Tangerang Selatan Tahun 2023",

        nama_tabel="rasio_belanja",

        api_url=f"{BASE_URL}?resource_id={RESOURCE_IDS['rasio_belanja']}",

        tahun=2023

    )

    records = get_rasio_belanja()

    clear_table(RasioBelanja)

    jumlah = 0

    for row in records:

        uraian = clean_string(
            row.get("Uraian")
        )

        if uraian == "":
            continue

        RasioBelanja.objects.create(

            dataset=dataset,

            uraian=uraian,

            pagu=to_int(
                row.get("Pagu")
            ),

            rasio=to_float(
                row.get("Rasio")
            )

        )

        jumlah += 1

    update_dataset(dataset, jumlah)

    print_success(
        "Rasio Belanja",
        jumlah
    )

def sync_realisasi_apbd():

    print("Sinkronisasi Dataset : Realisasi APBD")

    kategori = get_kategori("Ekonomi")

    dataset = get_dataset(
        kategori=kategori,
        nama_dataset="Jumlah Nilai Realisasi APBD Kota Tangerang Selatan Menurut Jenis Belanja Tahun 2022",
        nama_tabel="realisasi_apbd",
        api_url="-",
        tahun=2022,
    )

    # hapus data lama
    RealisasiAPBD.objects.filter(dataset=dataset).delete()

    file_csv = DATASET_DIR / "realisasi-apbd-menurut-jenis-belanja.csv"

    df = pd.read_csv(
        file_csv,
        sep=";",
        header=2,
        encoding="utf-8-sig"
    )

    jumlah = 0

    for _, row in df.iterrows():

        jenis = str(row.get("Jenis Belanja", "")).strip()

        # Lewati baris kosong
        if jenis == "" or jenis.lower() == "nan":
            continue

        # Lewati Total
        if jenis.lower() == "total":
            continue

        # Bersihkan nilai rupiah
        nilai2021 = (
            str(row.get("2021", "0"))
            .replace("Rp", "")
            .replace(".", "")
            .replace(",", "")
            .strip()
        )

        nilai2022 = (
            str(row.get("2022", "0"))
            .replace("Rp", "")
            .replace(".", "")
            .replace(",", "")
            .strip()
        )

        RealisasiAPBD.objects.create(
            dataset=dataset,
            jenis_belanja=jenis,
            tahun_2021=to_int(nilai2021),
            tahun_2022=to_int(nilai2022),
        )

        jumlah += 1

    dataset.jumlah_record = jumlah
    dataset.sinkron_terakhir = timezone.now()
    dataset.save()

    print(f"✓ Realisasi APBD ({jumlah} data)")

# ==========================================================
# SYNC REALISASI PERIZINAN
# ==========================================================

def sync_realisasi_perizinan():

    print("Sinkronisasi Dataset : Realisasi Perizinan")

    kategori = get_kategori("Ekonomi")

    dataset = get_dataset(

        kategori=kategori,

        nama_dataset="Jumlah Realisasi Perizinan Menurut Jenis di Kota Tangerang Selatan Tahun 2021",

        nama_tabel="realisasi_perizinan",

        api_url=f"{BASE_URL}?resource_id={RESOURCE_IDS['realisasi_perizinan']}",

        tahun=2021

    )

    clear_table(RealisasiPerizinan)

    records = get_realisasi_perizinan()

    jumlah = 0

    for row in records:

        nama = clean_string(
            row.get("Nama Izin")
        )

        if nama == "":
            continue

        RealisasiPerizinan.objects.create(

            dataset=dataset,

            nama_izin=nama,

            izin_masuk=to_int(
                row.get("Izin Masuk")
            ),

            izin_terbit=to_int(
                row.get("Izin Terbit")
            ),

            izin_ditolak=to_int(
                row.get("Izin Ditolak")
            ),

            dalam_proses=to_int(
                row.get("Dalam Proses")
            ),

        )

        jumlah += 1

    update_dataset(dataset, jumlah)

    print_success(
        "Realisasi Perizinan",
        jumlah
    )

# ==========================================================
# SYNC PROYEK INVESTASI
# ==========================================================

def sync_proyek_investasi():

    print("Sinkronisasi Dataset : Proyek Investasi")

    kategori = get_kategori("Ekonomi")

    dataset = get_dataset(

        kategori=kategori,

        nama_dataset="Jumlah Proyek Investasi PMA dan PMDN Menurut Sektor di Kota Tangerang Selatan Tahun 2020",

        nama_tabel="proyek_investasi",

        api_url=f"{BASE_URL}?resource_id={RESOURCE_IDS['proyek_investasi']}",

        tahun=2020

    )

    clear_table(ProyekInvestasi)

    records = get_proyek_investasi()

    jumlah = 0

    for row in records:

        sektor = clean_string(
            row.get("Sektor")
        )

        if sektor == "":
            continue

        ProyekInvestasi.objects.create(

            dataset=dataset,

            sektor=sektor,

            pma=to_int(
                row.get("PMA")
            ),

            pmdn=to_int(
                row.get("PMDN")
            ),

        )

        jumlah += 1

    update_dataset(dataset, jumlah)

    print_success(
        "Proyek Investasi",
        jumlah
    )

# ==========================================================
# SYNC SEMUA DATASET EKONOMI
# ==========================================================

def sync_semua_data_ekonomi():

    print("=" * 60)
    print("SINKRONISASI DATASET EKONOMI")
    print("=" * 60)

    sync_kelompok_perikanan()

    sync_umkm()

    sync_koperasi()

    sync_pajak_pariwisata()

    sync_rasio_belanja()

    sync_realisasi_apbd()

    sync_realisasi_perizinan()

    sync_proyek_investasi()

    print("=" * 60)
    print("SEMUA DATASET EKONOMI BERHASIL DISINKRONKAN")
    print("=" * 60)
import pandas as pd
from pathlib import Path

from django.utils import timezone

from dashboard.api import (
    get_penduduk_jenis_kelamin,
    get_penyandang_disabilitas,
)

from dashboard.models import (
    PendudukJenisKelamin,
    PenyandangDisabilitas,
    PendudukUsia6064,
    PPKSDTKS,
)

from dashboard.services.utils import (
    get_kategori,
    get_dataset,
    to_int,
)

# =====================================================
# LOKASI DATASET EXCEL
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "datasets"


# =====================================================
# PENDUDUK BERDASARKAN JENIS KELAMIN
# =====================================================

def sync_penduduk_jenis_kelamin():

    print("Sinkronisasi Dataset : Penduduk Berdasarkan Jenis Kelamin")

    kategori = get_kategori("Sosial")

    dataset = get_dataset(
        kategori=kategori,
        nama_dataset="Jumlah Penduduk Berdasarkan Jenis Kelamin",
        nama_tabel="penduduk_jenis_kelamin",
        api_url="https://data.tangerangselatankota.go.id/api/3/action/datastore_search?resource_id=e0d44b13-c1a8-411f-8469-1dedff7deedc",
        tahun=2023,
    )

    PendudukJenisKelamin.objects.filter(dataset=dataset).delete()

    data = get_penduduk_jenis_kelamin()

    jumlah = 0

    for row in data:

        nama = str(row.get("Nama Wilayah", "")).strip()

        # Lewati header & baris kosong
        if nama in ["", "Nama Wilayah", "(3)"]:
            continue

        # Lewati total kota
        if nama == "Kota Tangerang Selatan":
            continue

        PendudukJenisKelamin.objects.create(
            dataset=dataset,
            kecamatan=nama,
            laki_laki=to_int(row.get("Laki-Laki")),
            perempuan=to_int(row.get("Perempuan")),
            jumlah=to_int(row.get("Total")),
        )

        jumlah += 1

    dataset.jumlah_record = jumlah
    dataset.sinkron_terakhir = timezone.now()
    dataset.save()

    print(f"✓ Penduduk Berdasarkan Jenis Kelamin ({jumlah} data)")


# =====================================================
# PENDUDUK USIA 60-64
# =====================================================

def sync_penduduk_usia_6064():

    print("Sinkronisasi Dataset : Penduduk Usia 60-64 Tahun")

    kategori = get_kategori("Sosial")

    dataset = get_dataset(
        kategori=kategori,
        nama_dataset="Jumlah Penduduk Menurut Usia 60-64 Tahun",
        nama_tabel="penduduk_usia_6064",
        api_url="-",
        tahun=2023,
    )

    PendudukUsia6064.objects.filter(dataset=dataset).delete()

    file_excel = (
        DATASET_DIR /
        "jumlah-penduduk-menurut-usia-60-64-tahun.xlsx"
    )

    df = pd.read_excel(file_excel, header=1)

    df.columns = [
        "kode_wilayah",
        "nama_wilayah",
        "usia",
        "jumlah",
    ]

    jumlah = 0

    for _, row in df.iterrows():

        kode = str(row["kode_wilayah"]).strip()
        nama = str(row["nama_wilayah"]).strip()

        # Lewati baris nomor kolom
        if kode in ["", "nan", "(1)"]:
            continue

        # Lewati total kota
        if nama == "Kota Tangerang Selatan":
            continue

        # Lewati catatan sumber
        if kode.lower().startswith("sumber"):
            continue

        PendudukUsia6064.objects.create(
            dataset=dataset,
            kode_wilayah=kode,
            nama_wilayah=nama,
            usia=str(row["usia"]).strip(),
            jumlah=to_int(row["jumlah"]),
        )

        jumlah += 1

    dataset.jumlah_record = jumlah
    dataset.sinkron_terakhir = timezone.now()
    dataset.save()

    print(f"✓ Penduduk Usia 60-64 ({jumlah} data)")


# =====================================================
# PENYANDANG DISABILITAS
# =====================================================

def sync_penyandang_disabilitas():

    print("Sinkronisasi Dataset : Penyandang Disabilitas")

    kategori = get_kategori("Sosial")

    dataset = get_dataset(
        kategori=kategori,
        nama_dataset="Jumlah Penduduk Penyandang Disabilitas",
        nama_tabel="penyandang_disabilitas",
        api_url="https://data.tangerangselatankota.go.id/api/3/action/datastore_search?resource_id=78e1c90a-1185-47f0-a26f-139e6367acbf",
        tahun=2022,
    )

    PenyandangDisabilitas.objects.filter(dataset=dataset).delete()

    data = get_penyandang_disabilitas()

    jumlah = 0

    for row in data:

        PenyandangDisabilitas.objects.create(
            dataset=dataset,
            kecamatan=row.get("Kecamatan", ""),
            tuna_fisik=to_int(row.get("Tuna Fisik")),
            tuna_netra=to_int(row.get("Tuna Netra")),
            tuna_rungu_wicara=to_int(row.get("Tuna Rungu/Wicara")),
            tuna_mental_jiwa=to_int(row.get("Tuna Mental/Jiwa")),
            tuna_fisik_dan_mental=to_int(row.get("Tuna Fisik dan Mental")),
            lainnya=to_int(row.get("Lainnya")),
        )

        jumlah += 1

    dataset.jumlah_record = jumlah
    dataset.sinkron_terakhir = timezone.now()
    dataset.save()

    print(f"✓ Penyandang Disabilitas ({jumlah} data)")


# =====================================================
# PPKS DAN DTKS
# =====================================================

def sync_ppks_dtks():

    print("Sinkronisasi Dataset : PPKS dan DTKS")

    kategori = get_kategori("Sosial")

    dataset = get_dataset(
        kategori=kategori,
        nama_dataset="Persentase PPKS dan DTKS",
        nama_tabel="ppks_dtks",
        api_url="-",
        tahun=2022,
    )

    PPKSDTKS.objects.filter(dataset=dataset).delete()

    file_excel = (
        DATASET_DIR /
        "persentase-ppks-dan-dtks.xlsx"
    )

    df = pd.read_excel(file_excel, header=1)

    df.columns = [
        "kecamatan",
        "jumlah_ppks_mandiri",
        "persentase_dtks",
    ]

    jumlah = 0

    for _, row in df.iterrows():

        kecamatan = str(row["kecamatan"]).strip()

        if kecamatan.lower() == "kecamatan":
            continue

        if kecamatan in ["", "nan"]:
            continue

        PPKSDTKS.objects.create(
            dataset=dataset,
            kecamatan=kecamatan,
            jumlah_ppks_mandiri=to_int(row.get("jumlah_ppks_mandiri")),
            persentase_dtks=to_int(row.get("persentase_dtks")),
        )

        jumlah += 1

    dataset.jumlah_record = jumlah
    dataset.sinkron_terakhir = timezone.now()
    dataset.save()

    print(f"✓ PPKS & DTKS ({jumlah} data)")


# =====================================================
# SYNC SEMUA DATASET TAMBAHAN
# =====================================================

def sync_semua_data_tambahan():

    print("=" * 60)
    print("SINKRONISASI DATASET TAMBAHAN")
    print("=" * 60)

    sync_penduduk_usia_6064()
    sync_penduduk_jenis_kelamin()
    sync_penyandang_disabilitas()
    sync_ppks_dtks()

    print("=" * 60)
    print("SEMUA DATASET TAMBAHAN BERHASIL DISINKRONKAN")
    print("=" * 60)
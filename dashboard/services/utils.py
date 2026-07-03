from django.utils import timezone

from dashboard.models import (
    KategoriDataset,
    Dataset,
)


# ==========================================================
# MEMBUAT / MENGAMBIL KATEGORI
# ==========================================================

def get_kategori(nama):

    kategori, created = KategoriDataset.objects.get_or_create(
        nama_kategori=nama
    )

    return kategori


# ==========================================================
# MEMBUAT / MENGAMBIL DATASET
# ==========================================================

def get_dataset(
    kategori,
    nama_dataset,
    nama_tabel,
    api_url,
    tahun,
):

    dataset, created = Dataset.objects.get_or_create(

        nama_tabel=nama_tabel,

        defaults={

            "kategori": kategori,
            "nama_dataset": nama_dataset,
            "api_url": api_url,
            "tahun": tahun,
            "status": True,

        }

    )

    return dataset


# ==========================================================
# UPDATE METADATA DATASET
# ==========================================================

def update_dataset(dataset, jumlah_record):

    dataset.jumlah_record = jumlah_record

    dataset.sinkron_terakhir = timezone.now()

    dataset.save()


# ==========================================================
# HAPUS DATA LAMA
# ==========================================================

def clear_table(model):

    model.objects.all().delete()


# ==========================================================
# KONVERSI INTEGER
# ==========================================================

def to_int(value):

    if value is None:
        return 0

    value = str(value).strip()

    if value == "":
        return 0

    value = value.replace(".", "")
    value = value.replace(",", "")

    try:

        return int(float(value))

    except:

        return 0


# ==========================================================
# KONVERSI FLOAT
# ==========================================================

def to_float(value):

    if value is None:
        return 0

    value = str(value).strip()

    if value == "":
        return 0

    value = value.replace(".", "")
    value = value.replace(",", ".")

    try:

        return float(value)

    except:

        return 0


# ==========================================================
# MEMBERSIHKAN STRING
# ==========================================================

def clean_string(text):

    if text is None:
        return ""

    return str(text).strip()


# ==========================================================
# PRINT HASIL
# ==========================================================

def print_success(nama, jumlah):

    print(f"✓ {nama} ({jumlah} data)")
from dashboard.api import (
    get_siswa_miskin,
    get_air_minum,
    get_lahan,
    get_kesejahteraan,
    get_rumah,
    RESOURCE_IDS,
    BASE_URL,
)

from dashboard.models import (
    SiswaMiskin,
    AirMinum,
    Lahan,
    Rumah,
    Kesejahteraan,
)

from dashboard.services.utils import (
    get_kategori,
    get_dataset,
    update_dataset,
    clear_table,
    to_int,
    clean_string,
    print_success,
)


# ==========================================================
# SYNC SISWA MISKIN
# ==========================================================

def sync_siswa_miskin():

    print("Sinkronisasi Dataset : Siswa Miskin")

    # --------------------------------------
    # Membuat kategori
    # --------------------------------------

    kategori = get_kategori("Sosial")

    # --------------------------------------
    # Membuat metadata dataset
    # --------------------------------------

    dataset = get_dataset(

        kategori=kategori,

        nama_dataset="Jumlah Siswa Miskin Menurut Status dan Kecamatan di Kota Tangerang Selatan Tahun 2020",

        nama_tabel="siswa_miskin",

        api_url=f"{BASE_URL}?resource_id={RESOURCE_IDS['siswa_miskin']}",

        tahun=2020

    )

    # --------------------------------------
    # Ambil data dari API
    # --------------------------------------

    records = get_siswa_miskin()

    # --------------------------------------
    # Hapus data lama
    # --------------------------------------

    clear_table(SiswaMiskin)

    jumlah = 0

    # --------------------------------------
    # Simpan data baru
    # --------------------------------------

    for row in records:

        kecamatan = clean_string(
            row.get("KECAMATAN")
        )

        if kecamatan == "":
            continue

        SiswaMiskin.objects.create(

            dataset=dataset,

            kecamatan=kecamatan,

            m_aliyah=to_int(
                row.get("M Aliyah")
            ),

            m_ibtidaiyah=to_int(
                row.get("M Ibtidaiyah")
            ),

            m_tsanawiyah=to_int(
                row.get("M Tsanawiyah")
            ),

            paket_a=to_int(
                row.get("Paket A")
            ),

            paket_b=to_int(
                row.get("Paket B")
            ),

            paket_c=to_int(
                row.get("Paket C")
            ),

            perguruan_tinggi=to_int(
                row.get("Perguruan Tinggi")
            ),

            sd_sdlb=to_int(
                row.get("SD/SDLB")
            ),

            sma_smk_smalb=to_int(
                row.get("SMA/SMK /SMALB")
            ),

            smp_smplb=to_int(
                row.get("SMP/ SMPLB")
            ),

            lainnya=to_int(
                row.get("LAINNYA")
            ),

            grand_total=to_int(
                row.get("Grand Total")
            )

        )

        jumlah += 1

    # --------------------------------------
    # Update metadata dataset
    # --------------------------------------

    update_dataset(
        dataset,
        jumlah
    )

    print_success(
        "Siswa Miskin",
        jumlah
    )

# ==========================================================
# SYNC AIR MINUM
# ==========================================================

def sync_air_minum():

    print("Sinkronisasi Dataset : Air Minum")

    kategori = get_kategori("Sosial")

    dataset = get_dataset(

        kategori=kategori,

        nama_dataset="Jenis Air Minum yang Dikonsumsi Rumah Tangga Menurut Kecamatan di Kota Tangerang Selatan Tahun 2020",

        nama_tabel="air_minum",

        api_url=f"{BASE_URL}?resource_id={RESOURCE_IDS['air_minum']}",

        tahun=2020

    )

    records = get_air_minum()

    clear_table(AirMinum)

    jumlah = 0

    for row in records:

        kecamatan = clean_string(
            row.get("KECAMATAN")
        )

        if kecamatan == "":
            continue

        AirMinum.objects.create(

            dataset=dataset,

            kecamatan=kecamatan,

            air_isi_ulang=to_int(
                row.get("Air isi ulang")
            ),

            air_kemasan_bermerk=to_int(
                row.get("Air kemasan bermerk")
            ),

            air_sungai_danau_waduk=to_int(
                row.get("Air sungai/danau/waduk")
            ),

            lainnya=to_int(
                row.get("Lainnya")
            ),

            leding_eceran=to_int(
                row.get("Leding eceran")
            ),

            leding_meteran=to_int(
                row.get("Leding meteran")
            ),

            air_hujan=to_int(
                row.get("Air hujan")
            ),

            mata_air_tak_terlindung=to_int(
                row.get("Mata air tak terlindung")
            ),

            mata_air_terlindung=to_int(
                row.get("Mata air terlindung")
            ),

            sumur_bor_pompa=to_int(
                row.get("Sumur bor/pompa")
            ),

            sumur_tak_terlindung=to_int(
                row.get("Sumur tak terlindung")
            ),

            sumur_terlindung=to_int(
                row.get("Sumur terlindung")
            ),

            grand_total=to_int(
                row.get("Grand Total")
            )

        )

        jumlah += 1

    update_dataset(dataset, jumlah)

    print_success("Air Minum", jumlah)


# ==========================================================
# SYNC KEPEMILIKAN LAHAN
# ==========================================================

def sync_lahan():

    print("Sinkronisasi Dataset : Kepemilikan Lahan")

    kategori = get_kategori("Sosial")

    dataset = get_dataset(

        kategori=kategori,

        nama_dataset="Jumlah Kepemilikan Lahan Keluarga Menurut Status dan Kecamatan di Kota Tangerang Selatan Tahun 2020",

        nama_tabel="lahan",

        api_url=f"{BASE_URL}?resource_id={RESOURCE_IDS['lahan']}",

        tahun=2020

    )

    records = get_lahan()

    clear_table(Lahan)

    jumlah = 0

    for row in records:

        kecamatan = clean_string(
            row.get("KECAMATAN")
        )

        if kecamatan == "":
            continue

        Lahan.objects.create(

            dataset=dataset,

            kecamatan=kecamatan,

            milik_orang_lain=to_int(
                row.get("Milik orang lain")
            ),

            milik_sendiri=to_int(
                row.get("Milik sendiri")
            ),

            tanah_negara=to_int(
                row.get("Tanah negara")
            ),

            lainnya=to_int(
                row.get("Lainnya")
            ),

            grand_total=to_int(
                row.get("Grand Total")
            )

        )

        jumlah += 1

    update_dataset(dataset, jumlah)

    print_success("Kepemilikan Lahan", jumlah)

# ==========================================================
# SYNC STATUS KESEJAHTERAAN
# ==========================================================

def sync_kesejahteraan():

    print("Sinkronisasi Dataset : Status Kesejahteraan")

    kategori = get_kategori("Sosial")

    dataset = get_dataset(

        kategori=kategori,

        nama_dataset="Informasi Status Kesejahteraan Rumah Tangga dan Individu Menurut Kecamatan di Kota Tangerang Selatan Tahun 2020",

        nama_tabel="kesejahteraan",

        api_url=f"{BASE_URL}?resource_id={RESOURCE_IDS['kesejahteraan']}",

        tahun=2020

    )

    records = get_kesejahteraan()

    clear_table(Kesejahteraan)

    jumlah = 0

    for row in records:

        kecamatan = clean_string(
            row.get("KECAMATAN")
        )

        if kecamatan == "":
            continue

        Kesejahteraan.objects.create(

            dataset=dataset,

            kecamatan=kecamatan,

            laki_laki=to_int(
                row.get("Laki-laki")
            ),

            perempuan=to_int(
                row.get("Perempuan")
            ),

            grand_total=to_int(
                row.get("Grand Total")
            )

        )

        jumlah += 1

    update_dataset(dataset, jumlah)

    print_success(
        "Status Kesejahteraan",
        jumlah
    )


# ==========================================================
# SYNC KEPEMILIKAN RUMAH
# ==========================================================

def sync_rumah():

    print("Sinkronisasi Dataset : Kepemilikan Rumah")

    kategori = get_kategori("Sosial")

    dataset = get_dataset(

        kategori=kategori,

        nama_dataset="Jumlah Kepemilikan Rumah Keluarga Menurut Status dan Kecamatan di Kota Tangerang Selatan Tahun 2020",

        nama_tabel="rumah",

        api_url=f"{BASE_URL}?resource_id={RESOURCE_IDS['rumah']}",

        tahun=2020

    )

    records = get_rumah()

    clear_table(Rumah)

    jumlah = 0

    for row in records:

        kecamatan = clean_string(
            row.get("KECAMATAN")
        )

        if kecamatan == "":
            continue

        Rumah.objects.create(

            dataset=dataset,

            kecamatan=kecamatan,

            bebas_sewa=to_int(
                row.get("Bebas sewa")
            ),

            dinas=to_int(
                row.get("Dinas")
            ),

            kontrak_sewa=to_int(
                row.get("Kontrak/sewa")
            ),

            lainnya=to_int(
                row.get("Lainnya")
            ),

            milik_sendiri=to_int(
                row.get("Milik sendiri")
            ),

            grand_total=to_int(
                row.get("Grand Total")
            )

        )

        jumlah += 1

    update_dataset(dataset, jumlah)

    print_success(
        "Kepemilikan Rumah",
        jumlah
    )


# ==========================================================
# SYNC SELURUH DATASET SOSIAL
# ==========================================================

def sync_semua_data_sosial():

    print("=" * 60)
    print("SINKRONISASI DATASET SOSIAL")
    print("=" * 60)

    sync_siswa_miskin()

    sync_air_minum()

    sync_lahan()

    sync_kesejahteraan()

    sync_rumah()

    print("=" * 60)
    print("SEMUA DATASET SOSIAL BERHASIL DISINKRONKAN")
    print("=" * 60)
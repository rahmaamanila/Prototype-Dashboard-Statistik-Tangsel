from django.shortcuts import render
from django.http import HttpResponse
import json
import pandas as pd
from django.urls import reverse
import csv
from django.http import HttpResponse
from django.db.models import ForeignKey

from .models import (
    Dataset,
    SiswaMiskin,
    AirMinum,
    Lahan,
    Rumah,
    Kesejahteraan,
    PendudukUsia6064,
    PPKSDTKS,
    PendudukJenisKelamin,
    PenyandangDisabilitas,
    KelompokPerikanan,
    UMKM,
    Koperasi,
    PajakPariwisata,
    RasioBelanja,
    RealisasiPerizinan,
    ProyekInvestasi,
    RealisasiAPBD
)

# =====================================================
# DASHBOARD
# =====================================================

def home(request):

    siswa = SiswaMiskin.objects.all()
    rumah = Rumah.objects.all()
    lahan = Lahan.objects.all()
    sejahtera = Kesejahteraan.objects.all()
    air = AirMinum.objects.all()

    total_dataset = Dataset.objects.filter(status=True).count()

    # =====================================================
    # CHART SISWA MISKIN
    # =====================================================

    labels = [x.kecamatan for x in siswa]
    values = [x.grand_total for x in siswa]

    # =====================================================
    # CHART KEPEMILIKAN RUMAH
    # =====================================================

    rumah_labels = [
        "Milik Sendiri",
        "Kontrak/Sewa",
        "Lainnya",
        "Bebas Sewa",
        "Dinas",
    ]

    rumah_values = [
        sum(x.milik_sendiri for x in rumah),
        sum(x.kontrak_sewa for x in rumah),
        sum(x.lainnya for x in rumah),
        sum(x.bebas_sewa for x in rumah),
        sum(x.dinas for x in rumah),
    ]

    # =====================================================
    # CHART KEPEMILIKAN LAHAN
    # =====================================================

    lahan_labels = [
        "Milik Sendiri",
        "Milik Orang Lain",
        "Tanah Negara",
        "Lainnya",
    ]

    lahan_values = [
        sum(x.milik_sendiri for x in lahan),
        sum(x.milik_orang_lain for x in lahan),
        sum(x.tanah_negara for x in lahan),
        sum(x.lainnya for x in lahan),
    ]

    # =====================================================
    # CHART STATUS KESEJAHTERAAN
    # =====================================================

    sejahtera_labels = [x.kecamatan for x in sejahtera]
    laki_values = [x.laki_laki for x in sejahtera]
    perempuan_values = [x.perempuan for x in sejahtera]

    # =====================================================
    # CHART AIR MINUM
    # =====================================================

    air_labels = [
        "Air Isi Ulang",
        "Air Kemasan",
        "Air Sungai",
        "Lainnya",
        "Leding Eceran",
        "Leding Meteran",
        "Air Hujan",
        "Mata Air Tak Terlindung",
        "Mata Air Terlindung",
        "Sumur Bor/Pompa",
        "Sumur Tak Terlindung",
        "Sumur Terlindung",
    ]

    air_values = [
        sum(x.air_isi_ulang for x in air),
        sum(x.air_kemasan_bermerk for x in air),
        sum(x.air_sungai_danau_waduk for x in air),
        sum(x.lainnya for x in air),
        sum(x.leding_eceran for x in air),
        sum(x.leding_meteran for x in air),
        sum(x.air_hujan for x in air),
        sum(x.mata_air_tak_terlindung for x in air),
        sum(x.mata_air_terlindung for x in air),
        sum(x.sumur_bor_pompa for x in air),
        sum(x.sumur_tak_terlindung for x in air),
        sum(x.sumur_terlindung for x in air),
    ]

    # =====================================================
    # CHART PENDUDUK USIA 60-64
    # =====================================================

    usia6064 = PendudukUsia6064.objects.all()

    usia_labels = [x.nama_wilayah.replace("Kecamatan ", "") for x in usia6064]
    usia_values = [x.jumlah for x in usia6064]

    # =====================================================
    # CHART Penduduk Berdasarkan Jenis Kelamin
    # =====================================================

    penduduk = PendudukJenisKelamin.objects.all()

    jk_labels = [x.kecamatan for x in penduduk]

    laki = [x.laki_laki for x in penduduk]

    perempuan = [x.perempuan for x in penduduk]

    # =====================================================
    # CHART Penyandang Disabilitas
    # =====================================================

    disabilitas = PenyandangDisabilitas.objects.all()

    dis_labels = [x.kecamatan for x in disabilitas]

    tuna_fisik = [x.tuna_fisik for x in disabilitas]
    tuna_netra = [x.tuna_netra for x in disabilitas]
    tuna_rungu = [x.tuna_rungu_wicara for x in disabilitas]
    tuna_mental = [x.tuna_mental_jiwa for x in disabilitas]
    ganda = [x.tuna_fisik_dan_mental for x in disabilitas]
    lainnya = [x.lainnya for x in disabilitas]

    # =====================================================
    # CHART PPKS dan DTKS
    # =====================================================

    ppks = PPKSDTKS.objects.all()

    ppks_labels = [x.kecamatan.title() for x in ppks]

    ppks_values = [x.persentase_dtks for x in ppks]


    # =====================================================
    # CHART UMKM
    # =====================================================

    umkm = UMKM.objects.all()

    umkm_labels = [x.kecamatan for x in umkm]
    umkm_values = [x.jumlah_umkm for x in umkm]


    # =====================================================
    # CHART KELOMPOK PERIKANAN
    # =====================================================

    perikanan = KelompokPerikanan.objects.all()

    perikanan_labels = [x.kecamatan for x in perikanan]

    pengolah = [x.pengolah for x in perikanan]
    pemasaran = [x.pemasaran for x in perikanan]


    # =====================================================
    # CHART PROYEK INVESTASI
    # =====================================================

    investasi = ProyekInvestasi.objects.all()

    investasi_labels = [x.sektor for x in investasi]

    pma = [x.pma for x in investasi]
    pmdn = [x.pmdn for x in investasi]


    # =====================================================
    # CHART REALISASI PERIZINAN
    # =====================================================

    izin = RealisasiPerizinan.objects.all()

    izin_labels = [x.nama_izin for x in izin]

    izin_masuk = [x.izin_masuk for x in izin]
    izin_terbit = [x.izin_terbit for x in izin]
    

    # =====================================================
    # CHART PAJAK PARIWISATA
    # =====================================================

    pajak = PajakPariwisata.objects.all()

    pajak_labels = [
        f"{x.tahun} - {x.jenis_pajak}"
        for x in pajak
    ]

    pajak_values = [
        x.realisasi
        for x in pajak
    ]

    # =====================================================
    # CHART REALISASI APBD
    # =====================================================

    apbd = RealisasiAPBD.objects.all()

    apbd_labels = [x.jenis_belanja for x in apbd]

    apbd_2021 = [x.tahun_2021 for x in apbd]

    apbd_2022 = [x.tahun_2022 for x in apbd]


    # =====================================================
    # CHART RASIO BELANJA
    # =====================================================

    rasio = RasioBelanja.objects.all()

    rasio_labels = [x.uraian for x in rasio]

    rasio_values = [x.rasio for x in rasio]


    # =====================================================
    # CHART RASIO BELANJA
    # =====================================================

    rasio = RasioBelanja.objects.all()

    rasio_labels = [x.uraian for x in rasio]

    rasio_values = [x.rasio for x in rasio]

    # =====================================================
    # CHART KOPERASI
    # =====================================================

    koperasi = Koperasi.objects.all()

    koperasi_labels = [
        x.jumlah_aset
        for x in koperasi
    ]

    koperasi_values = [
        x.jumlah
        for x in koperasi
    ]


    context = {

        # "api_status": "Database",

        # "api_badge": "success",

        # "api_icon": "fas fa-database",

        "total_dataset": total_dataset,

        "jumlah_siswa": siswa.count(),

        "jumlah_rumah": rumah.count(),

        "jumlah_lahan": lahan.count(),

        "jumlah_sejahtera": sejahtera.count(),

        "jumlah_air": air.count(),

        "labels": json.dumps(labels),
        "values": json.dumps(values),

        "rumah_labels": json.dumps(rumah_labels),
        "rumah_values": json.dumps(rumah_values),

        "lahan_labels": json.dumps(lahan_labels),
        "lahan_values": json.dumps(lahan_values),

        "sejahtera_labels": json.dumps(sejahtera_labels),
        "laki_values": json.dumps(laki_values),
        "perempuan_values": json.dumps(perempuan_values),

        "air_labels": json.dumps(air_labels),
        "air_values": json.dumps(air_values),

        "usia_labels": json.dumps(usia_labels),
        "usia_values": json.dumps(usia_values),

        "jk_labels": json.dumps(jk_labels),
        "jk_laki": json.dumps(laki),
        "jk_perempuan": json.dumps(perempuan),

        "dis_labels": json.dumps(dis_labels),

        "tuna_fisik": json.dumps(tuna_fisik),
        "tuna_netra": json.dumps(tuna_netra),
        "tuna_rungu": json.dumps(tuna_rungu),
        "tuna_mental": json.dumps(tuna_mental),
        "tuna_ganda": json.dumps(ganda),
        "tuna_lain": json.dumps(lainnya),

        "ppks_labels": json.dumps(ppks_labels),
        "ppks_values": json.dumps(ppks_values),

        "umkm_labels": json.dumps(umkm_labels),
        "umkm_values": json.dumps(umkm_values),

        "perikanan_labels": json.dumps(perikanan_labels),
        "pengolah": json.dumps(pengolah),
        "pemasaran": json.dumps(pemasaran),

        "investasi_labels": json.dumps(investasi_labels),
        "pma": json.dumps(pma),
        "pmdn": json.dumps(pmdn),

        "izin_labels": json.dumps(izin_labels),
        "izin_masuk": json.dumps(izin_masuk),
        "izin_terbit": json.dumps(izin_terbit),

        "pajak_labels": json.dumps(pajak_labels),
        "pajak_values": json.dumps(pajak_values),

        "apbd_labels": json.dumps(apbd_labels),
        "apbd_2021": json.dumps(apbd_2021),
        "apbd_2022": json.dumps(apbd_2022),

        "rasio_labels": json.dumps(rasio_labels),
        "rasio_values": json.dumps(rasio_values),

        "koperasi_labels": json.dumps(koperasi_labels),
        "koperasi_values": json.dumps(koperasi_values),

    }

    return render(request, "dashboard/home.html", context)





# =====================================================
# HELPER EXPORT EXCEL
# =====================================================

def queryset_to_excel(queryset, fields=None):

    if fields:
        return pd.DataFrame(
            list(queryset.values(*fields))
        )

    return pd.DataFrame(
        list(queryset.values())
    )

# =====================================================
# HALAMAN SISWA MISKIN
# =====================================================

def siswa(request):

    queryset = SiswaMiskin.objects.all()

    data = []

    for item in queryset:

        data.append({
            "kecamatan": item.kecamatan,
            "sd": item.sd_sdlb,
            "smp": item.smp_smplb,
            "sma": item.sma_smk_smalb,
            "aliyah": item.m_aliyah,
            "ibtidaiyah": item.m_ibtidaiyah,
            "tsanawiyah": item.m_tsanawiyah,
            "paket_a": item.paket_a,
            "paket_b": item.paket_b,
            "paket_c": item.paket_c,
            "pt": item.perguruan_tinggi,
            "lainnya": item.lainnya,
            "total": item.grand_total,
        })

    context = {

        "jumlah_siswa": queryset.count(),

        "jumlah_kecamatan": queryset.count(),

        "tahun": "2020",

        "data": data,

        "labels": json.dumps([x["kecamatan"] for x in data]),

        "total": json.dumps([x["total"] for x in data]),

        "sd": json.dumps([x["sd"] for x in data]),

        "smp": json.dumps([x["smp"] for x in data]),

        "sma": json.dumps([x["sma"] for x in data]),

        "aliyah": json.dumps([x["aliyah"] for x in data]),

        "ibtidaiyah": json.dumps([x["ibtidaiyah"] for x in data]),

        "tsanawiyah": json.dumps([x["tsanawiyah"] for x in data]),

        "paket_a": json.dumps([x["paket_a"] for x in data]),

        "paket_b": json.dumps([x["paket_b"] for x in data]),

        "paket_c": json.dumps([x["paket_c"] for x in data]),

        "pt": json.dumps([x["pt"] for x in data]),

        "lainnya": json.dumps([x["lainnya"] for x in data]),

        "api_endpoint": "/api/siswa-miskin/",
        "api_dataset": "Jumlah Siswa Miskin",
    }

    return render(
        request,
        "dashboard/siswa_miskin.html",
        context,
    )


# =====================================================
# DOWNLOAD SISWA MISKIN
# =====================================================

def download_siswa(request):

    df = queryset_to_excel(
        SiswaMiskin.objects.all(),
        fields=[
            "kecamatan",
            "m_aliyah",
            "m_ibtidaiyah",
            "m_tsanawiyah",
            "paket_a",
            "paket_b",
            "paket_c",
            "perguruan_tinggi",
            "sd_sdlb",
            "sma_smk_smalb",
            "smp_smplb",
            "lainnya",
            "grand_total",
        ]
    )

    df.columns = [
        "KECAMATAN",
        "M Aliyah",
        "M Ibtidaiyah",
        "M Tsanawiyah",
        "Paket A",
        "Paket B",
        "Paket C",
        "Perguruan Tinggi",
        "SD/SDLB",
        "SMA/SMK /SMALB",
        "SMP/ SMPLB",
        "LAINNYA",
        "Grand Total",
    ]

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="siswa_miskin.xlsx"'
    )

    df.to_excel(
        response,
        index=False,
        engine="openpyxl",
    )

    return response


# =====================================================
# HALAMAN AIR MINUM
# =====================================================

def air_minum(request):

    queryset = AirMinum.objects.all()

    data = []

    for item in queryset:

        data.append({

            "kecamatan": item.kecamatan,

            "air_isi": item.air_isi_ulang,

            "air_kemasan": item.air_kemasan_bermerk,

            "air_sungai": item.air_sungai_danau_waduk,

            "lainnya": item.lainnya,

            "leding_eceran": item.leding_eceran,

            "leding_meteran": item.leding_meteran,

            "air_hujan": item.air_hujan,

            "mata_air_tak": item.mata_air_tak_terlindung,

            "mata_air_ter": item.mata_air_terlindung,

            "sumur_bor": item.sumur_bor_pompa,

            "sumur_tak": item.sumur_tak_terlindung,

            "sumur_ter": item.sumur_terlindung,

            "total": item.grand_total,
        })

    context = {

        "jumlah_air_minum": queryset.count(),

        "jumlah_kecamatan": queryset.count(),

        "tahun": "2020",

        "data": data,

        "labels": json.dumps([x["kecamatan"] for x in data]),

        "total": json.dumps([x["total"] for x in data]),

        "air_isi": json.dumps([x["air_isi"] for x in data]),

        "air_kemasan": json.dumps([x["air_kemasan"] for x in data]),

        "air_sungai": json.dumps([x["air_sungai"] for x in data]),

        "lainnya": json.dumps([x["lainnya"] for x in data]),

        "leding_eceran": json.dumps([x["leding_eceran"] for x in data]),

        "leding_meteran": json.dumps([x["leding_meteran"] for x in data]),

        "air_hujan": json.dumps([x["air_hujan"] for x in data]),

        "mata_air_tak": json.dumps([x["mata_air_tak"] for x in data]),

        "mata_air_ter": json.dumps([x["mata_air_ter"] for x in data]),

        "sumur_bor": json.dumps([x["sumur_bor"] for x in data]),

        "sumur_tak": json.dumps([x["sumur_tak"] for x in data]),

        "sumur_ter": json.dumps([x["sumur_ter"] for x in data]),

        "api_endpoint": "/api/air-minum/",
        "api_dataset": "Jenis Air Minum",
    }

    return render(
        request,
        "dashboard/air_minum.html",
        context,
    )


# =====================================================
# DOWNLOAD AIR MINUM
# =====================================================

def download_air(request):

    df = queryset_to_excel(
        AirMinum.objects.all(),
        fields=[
            "kecamatan",
            "air_isi_ulang",
            "air_kemasan_bermerk",
            "air_sungai_danau_waduk",
            "lainnya",
            "leding_eceran",
            "leding_meteran",
            "air_hujan",
            "mata_air_tak_terlindung",
            "mata_air_terlindung",
            "sumur_bor_pompa",
            "sumur_tak_terlindung",
            "sumur_terlindung",
            "grand_total",
        ]
    )

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="air_minum.xlsx"'
    )

    df.to_excel(
        response,
        index=False,
        engine="openpyxl",
    )

    return response

# =====================================================
# HALAMAN KEPEMILIKAN LAHAN
# =====================================================

def lahan(request):

    queryset = Lahan.objects.all()

    data = []

    for item in queryset:

        data.append({
            "kecamatan": item.kecamatan,
            "milik_sendiri": item.milik_sendiri,
            "milik_orang_lain": item.milik_orang_lain,
            "tanah_negara": item.tanah_negara,
            "lainnya": item.lainnya,
            "total": item.grand_total,
        })

    context = {

        "jumlah_lahan": queryset.count(),

        "jumlah_kecamatan": queryset.count(),

        "tahun": "2020",

        "data": data,

        "labels": json.dumps([x["kecamatan"] for x in data]),

        "total": json.dumps([x["total"] for x in data]),

        "milik_sendiri": json.dumps([x["milik_sendiri"] for x in data]),

        "milik_orang_lain": json.dumps([x["milik_orang_lain"] for x in data]),

        "tanah_negara": json.dumps([x["tanah_negara"] for x in data]),

        "lainnya": json.dumps([x["lainnya"] for x in data]),

        "api_endpoint": "/api/kepemilikan-lahan/",
        "api_dataset": "Kepemilikan Lahan",
    }

    return render(
        request,
        "dashboard/lahan.html",
        context,
    )


# =====================================================
# DOWNLOAD LAHAN
# =====================================================

def download_lahan(request):

    df = queryset_to_excel(
        Lahan.objects.all(),
        fields=[
            "kecamatan",
            "milik_sendiri",
            "milik_orang_lain",
            "tanah_negara",
            "lainnya",
            "grand_total",
        ]
    )

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="kepemilikan_lahan.xlsx"'
    )

    df.to_excel(
        response,
        index=False,
        engine="openpyxl",
    )

    return response


# =====================================================
# HALAMAN STATUS KESEJAHTERAAN
# =====================================================

def kesejahteraan(request):

    queryset = Kesejahteraan.objects.all()

    data = []

    for item in queryset:

        data.append({

            "kecamatan": item.kecamatan,

            "laki": item.laki_laki,

            "perempuan": item.perempuan,

            "total": item.grand_total,
        })

    context = {

        "jumlah_kesejahteraan": queryset.count(),

        "jumlah_kecamatan": queryset.count(),

        "tahun": "2020",

        "data": data,

        "labels": json.dumps([x["kecamatan"] for x in data]),

        "total": json.dumps([x["total"] for x in data]),

        "laki": json.dumps([x["laki"] for x in data]),

        "perempuan": json.dumps([x["perempuan"] for x in data]),
        
        "api_endpoint": "/api/status_kesejahteraan/",
        "api_dataset": "Status Kesejahteraan",
    }

    return render(
        request,
        "dashboard/kesejahteraan.html",
        context,
    )


# =====================================================
# DOWNLOAD STATUS KESEJAHTERAAN
# =====================================================

def download_kesejahteraan(request):

    df = queryset_to_excel(
        Kesejahteraan.objects.all(),
        fields=[
            "kecamatan",
            "laki_laki",
            "perempuan",
            "grand_total",
        ]
    )

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="status_kesejahteraan.xlsx"'
    )

    df.to_excel(
        response,
        index=False,
        engine="openpyxl",
    )

    return response


# =====================================================
# HALAMAN KEPEMILIKAN RUMAH
# =====================================================

def rumah(request):

    queryset = Rumah.objects.all()

    data = []

    for item in queryset:

        data.append({

            "kecamatan": item.kecamatan,

            "milik_sendiri": item.milik_sendiri,

            "kontrak": item.kontrak_sewa,

            "bebas_sewa": item.bebas_sewa,

            "dinas": item.dinas,

            "lainnya": item.lainnya,

            "total": item.grand_total,
        })

    context = {

        "jumlah_rumah": queryset.count(),

        "jumlah_kecamatan": queryset.count(),

        "tahun": "2020",

        "data": data,

        "labels": json.dumps([x["kecamatan"] for x in data]),

        "total": json.dumps([x["total"] for x in data]),

        "milik_sendiri": json.dumps([x["milik_sendiri"] for x in data]),

        "kontrak": json.dumps([x["kontrak"] for x in data]),

        "bebas_sewa": json.dumps([x["bebas_sewa"] for x in data]),

        "dinas": json.dumps([x["dinas"] for x in data]),

        "lainnya": json.dumps([x["lainnya"] for x in data]),

        "api_endpoint": "/api/kepemilikan-rumah/",
        "api_dataset": "Kepemilikan Rumah",
    }

    return render(
        request,
        "dashboard/rumah.html",
        context,
    )


# =====================================================
# DOWNLOAD RUMAH
# =====================================================

def download_rumah(request):

    df = queryset_to_excel(
        Rumah.objects.all(),
        fields=[
            "kecamatan",
            "milik_sendiri",
            "kontrak_sewa",
            "bebas_sewa",
            "dinas",
            "lainnya",
            "grand_total",
        ]
    )

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="kepemilikan_rumah.xlsx"'
    )

    df.to_excel(
        response,
        index=False,
        engine="openpyxl",
    )

    return response

# =====================================================
# HALAMAN USIA 60-64 TAHUN
# =====================================================

def usia_60_64(request):

    queryset = PendudukUsia6064.objects.all()

    data = []

    for item in queryset:

        data.append({

            "kode": item.kode_wilayah,

            "wilayah": item.nama_wilayah,

            "usia": item.usia,

            "jumlah": item.jumlah,

        })

    context = {

        "jumlah_data": queryset.count(),

        "jumlah_kecamatan": queryset.count(),

        "tahun": "2024",

        "data": data,

        "labels": json.dumps([x["wilayah"] for x in data]),

        "jumlah": json.dumps([x["jumlah"] for x in data]),

        "api_endpoint": "/api/penduduk-usia/",
        "api_dataset": "Penduduk Usia",

    }

    return render(
        request,
        "dashboard/usia_60_64.html",
        context,
    )

# =====================================================
# DOWNLOAD USIA 60-64
# =====================================================

def download_usia_60_64(request):

    df = queryset_to_excel(
        PendudukUsia6064.objects.all(),
        fields=[
            "kode_wilayah",
            "nama_wilayah",
            "usia",
            "jumlah",
        ]
    )

    df.columns = [
        "Kode Wilayah",
        "Nama Wilayah",
        "Usia",
        "Jumlah",
    ]

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="usia_60_64.xlsx"'
    )

    df.to_excel(
        response,
        index=False,
        engine="openpyxl",
    )

    return response

# =====================================================
# HALAMAN PPKS & DTKS
# =====================================================

def ppks_dtks(request):

    queryset = PPKSDTKS.objects.all()

    data = []

    for item in queryset:

        data.append({

            "kecamatan": item.kecamatan,

            "ppks": item.jumlah_ppks_mandiri,

            "dtks": item.persentase_dtks,

        })

    context = {

        "jumlah_data": queryset.count(),

        "jumlah_kecamatan": queryset.count(),

        "tahun": "2020",

        "data": data,

        "labels": json.dumps(
            [x["kecamatan"] for x in data]
        ),

        "dtks": json.dumps(
            [x["dtks"] for x in data]
        ),

        "api_endpoint": "/api/ppks-dtks/",
        "api_dataset": "PPKS DTKS",

    }

    return render(

        request,

        "dashboard/ppks_dtks.html",

        context,

    )

# =====================================================
# DOWNLOAD PPKS & DTKS
# =====================================================

def download_ppks_dtks(request):

    df = queryset_to_excel(

        PPKSDTKS.objects.all(),

        fields=[

            "kecamatan",

            "jumlah_ppks_mandiri",

            "persentase_dtks",

        ]

    )

    response = HttpResponse(

        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    response["Content-Disposition"] = (

        'attachment; filename="ppks_dtks.xlsx"'

    )

    df.to_excel(

        response,

        index=False,

        engine="openpyxl",

    )

    return response

# =====================================================
# HALAMAN PENDUDUK BERDASARKAN JENIS KELAMIN
# =====================================================

def penduduk_jenis_kelamin(request):

    queryset = PendudukJenisKelamin.objects.all()

    data = []

    for item in queryset:

        data.append({
            "kode": item.kode_wilayah,

            "kecamatan": item.kecamatan,

            "laki_laki": item.laki_laki,

            "perempuan": item.perempuan,

            "jumlah": item.jumlah,

        })

    context = {

        "jumlah_data": queryset.count(),

        "jumlah_kecamatan": queryset.count(),

        "tahun": "2024",

        "data": data,

        "labels": json.dumps([x["kecamatan"] for x in data]),

        "laki_laki": json.dumps([x["laki_laki"] for x in data]),

        "perempuan": json.dumps([x["perempuan"] for x in data]),

        "jumlah": json.dumps([x["jumlah"] for x in data]),

        "api_endpoint": "/api/penduduk-jenis-kelamin/",
        "api_dataset": "Penduduk Jenis Kelamin",

    }

    return render(

        request,

        "dashboard/jenis_kelamin.html",

        context,

    )

# =====================================================
# DOWNLOAD PENDUDUK BERDASARKAN JENIS KELAMIN
# =====================================================

def download_penduduk_jenis_kelamin(request):

    df = queryset_to_excel(

        PendudukJenisKelamin.objects.all(),

        fields=[
            "kode_wilayah",

            "kecamatan",

            "laki_laki",

            "perempuan",

            "jumlah",

        ]

    )

    response = HttpResponse(

        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    response["Content-Disposition"] = (

        'attachment; filename="penduduk_jenis_kelamin.xlsx"'

    )

    df.to_excel(

        response,

        index=False,

        engine="openpyxl",

    )

    return response

# =====================================================
# HALAMAN PENYANDANG DISABILITAS
# =====================================================

def disabilitas(request):

    queryset = PenyandangDisabilitas.objects.all()

    data = []

    for item in queryset:

        total = (
            item.tuna_fisik
            + item.tuna_netra
            + item.tuna_rungu_wicara
            + item.tuna_mental_jiwa
            + item.tuna_fisik_dan_mental
            + item.lainnya
        )

        data.append({

            "kecamatan": item.kecamatan,

            "tuna_fisik": item.tuna_fisik,

            "tuna_netra": item.tuna_netra,

            "tuna_rungu_wicara": item.tuna_rungu_wicara,

            "tuna_mental_jiwa": item.tuna_mental_jiwa,

            "tuna_fisik_dan_mental": item.tuna_fisik_dan_mental,

            "lainnya": item.lainnya,

            "total": total,

        })

    context = {

        "jumlah_data": queryset.count(),

        "jumlah_kecamatan": queryset.count(),

        "tahun": "2024",

        "data": data,

        "labels": json.dumps([x["kecamatan"] for x in data]),

        "total": json.dumps([x["total"] for x in data]),

        "tuna_fisik": json.dumps([x["tuna_fisik"] for x in data]),

        "tuna_netra": json.dumps([x["tuna_netra"] for x in data]),

        "tuna_rungu_wicara": json.dumps([x["tuna_rungu_wicara"] for x in data]),

        "tuna_mental_jiwa": json.dumps([x["tuna_mental_jiwa"] for x in data]),

        "tuna_fisik_dan_mental": json.dumps([x["tuna_fisik_dan_mental"] for x in data]),

        "lainnya": json.dumps([x["lainnya"] for x in data]),

        "api_endpoint": "/api/penyandang-disabilitas/",
        "api_dataset": "Penyandang Disabilitas",

    }

    return render(

        request,

        "dashboard/disabilitas.html",

        context,

    )

# =====================================================
# DOWNLOAD PENYANDANG DISABILITAS
# =====================================================

def download_disabilitas(request):

    df = queryset_to_excel(

        PenyandangDisabilitas.objects.all(),

        fields=[

            "kecamatan",

            "tuna_fisik",

            "tuna_netra",

            "tuna_rungu_wicara",

            "tuna_mental_jiwa",

            "tuna_fisik_dan_mental",

            "lainnya",

        ]

    )

    response = HttpResponse(

        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    response["Content-Disposition"] = (

        'attachment; filename="penyandang_disabilitas.xlsx"'

    )

    df.to_excel(

        response,

        index=False,

        engine="openpyxl",

    )

    return response

# =====================================================
# HALAMAN KELOMPOK PERIKANAN
# =====================================================

def kelompok_perikanan(request):

    queryset = KelompokPerikanan.objects.all()

    data = []

    for item in queryset:

        total = item.pengolah + item.pemasaran

        data.append({

            "kecamatan": item.kecamatan,

            "pengolah": item.pengolah,

            "pemasaran": item.pemasaran,

            "total": total,

        })

    context = {

        "jumlah_data": queryset.count(),

        "jumlah_kecamatan": queryset.count(),

        "tahun": "2024",

        "data": data,

        "labels": json.dumps([x["kecamatan"] for x in data]),

        "total": json.dumps([x["total"] for x in data]),

        "pengolah": json.dumps([x["pengolah"] for x in data]),

        "pemasaran": json.dumps([x["pemasaran"] for x in data]),

        "api_endpoint": "/api/kelompok-perikanan/",
        "api_dataset": "Kelompok Perikanan",

    }

    return render(

        request,

        "dashboard/kelompok_perikanan.html",

        context,

    )

# =====================================================
# DOWNLOAD KELOMPOK PERIKANAN
# =====================================================

def download_kelompok_perikanan(request):

    df = queryset_to_excel(

        KelompokPerikanan.objects.all(),

        fields=[

            "kecamatan",

            "pengolah",

            "pemasaran",

        ]

    )

    response = HttpResponse(

        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    response["Content-Disposition"] = (

        'attachment; filename="kelompok_perikanan.xlsx"'

    )

    df.to_excel(

        response,

        index=False,

        engine="openpyxl",

    )

    return response

# =====================================================
# HALAMAN UMKM
# =====================================================

def umkm(request):

    queryset = UMKM.objects.all()

    data = []

    for item in queryset:

        data.append({

            "kecamatan": item.kecamatan,

            "jumlah_umkm": item.jumlah_umkm,

        })

    context = {

        "jumlah_data": queryset.count(),

        "jumlah_kecamatan": queryset.count(),

        "tahun": "2024",

        "data": data,

        "labels": json.dumps([x["kecamatan"] for x in data]),

        "jumlah_umkm": json.dumps(
            [x["jumlah_umkm"] for x in data]
        ),

        "api_endpoint": "/api/umkm/",
        "api_dataset": "UMKM",

    }

    return render(

        request,

        "dashboard/umkm.html",

        context,

    )

# =====================================================
# DOWNLOAD UMKM
# =====================================================

def download_umkm(request):

    df = queryset_to_excel(

        UMKM.objects.all(),

        fields=[

            "kecamatan",

            "jumlah_umkm",

        ]

    )

    response = HttpResponse(

        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    response["Content-Disposition"] = (

        'attachment; filename="umkm.xlsx"'

    )

    df.to_excel(

        response,

        index=False,

        engine="openpyxl",

    )

    return response

# =====================================================
# HALAMAN KOPERASI
# =====================================================

def koperasi(request):

    queryset = Koperasi.objects.all()

    data = []

    for item in queryset:

        data.append({

            "jumlah_aset": item.jumlah_aset,

            "jumlah": item.jumlah,

        })

    context = {

        "jumlah_data": queryset.count(),

        "jumlah_kategori": queryset.count(),

        "tahun": "2024",

        "data": data,

        "labels": json.dumps(
            [x["jumlah_aset"] for x in data]
        ),

        "jumlah": json.dumps(
            [x["jumlah"] for x in data]
        ),

        "api_endpoint": "/api/koperasi/",
        "api_dataset": "Koperasi",

    }

    return render(

        request,

        "dashboard/koperasi.html",

        context,

    )

# =====================================================
# DOWNLOAD KOPERASI
# =====================================================

def download_koperasi(request):

    df = pd.DataFrame(

        list(

            Koperasi.objects.all().values(

                "jumlah_aset",

                "jumlah",

            )

        )

    )

    response = HttpResponse(

        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    response["Content-Disposition"] = (

        'attachment; filename="koperasi.xlsx"'

    )

    df.to_excel(

        response,

        index=False,

        engine="openpyxl",

    )

    return response

# =====================================================
# HALAMAN PAJAK PARIWISATA
# =====================================================

def pajak_pariwisata(request):

    queryset = PajakPariwisata.objects.all().order_by(
        "tahun",
        "jenis_pajak"
    )

    data = []

    labels = []

    realisasi = []

    hotel = []

    restoran = []

    hiburan = []

    tahun_list = []

    for item in queryset:

        data.append({

            "tahun": item.tahun,

            "jenis_pajak": item.jenis_pajak,

            "realisasi": item.realisasi,

        })

        labels.append(
            f"{item.tahun}\n{item.jenis_pajak}"
        )

        realisasi.append(item.realisasi)

    for tahun in [2018, 2019, 2020, 2021]:

        tahun_list.append(str(tahun))

        hotel_data = queryset.filter(
            tahun=tahun,
            jenis_pajak="Pajak Hotel"
        ).first()

        restoran_data = queryset.filter(
            tahun=tahun,
            jenis_pajak="Pajak Restoran"
        ).first()

        hiburan_data = queryset.filter(
            tahun=tahun,
            jenis_pajak="Pajak Hiburan"
        ).first()

        hotel.append(
            hotel_data.realisasi if hotel_data else 0
        )

        restoran.append(
            restoran_data.realisasi if restoran_data else 0
        )

        hiburan.append(
            hiburan_data.realisasi if hiburan_data else 0
        )

    context = {

        "jumlah_data": queryset.count(),

        "jumlah_tahun": 4,

        "tahun": "2018-2021",

        "data": data,

        "labels": json.dumps(labels),

        "realisasi": json.dumps(realisasi),

        "tahun_labels": json.dumps(tahun_list),

        "hotel": json.dumps(hotel),

        "restoran": json.dumps(restoran),

        "hiburan": json.dumps(hiburan),

        "api_endpoint": "/api/pajak-pariwisata/",
        "api_dataset": "Pajak Pariwisata",

    }

    return render(

        request,

        "dashboard/pajak_pariwisata.html",

        context,

    )

# =====================================================
# DOWNLOAD PAJAK PARIWISATA
# =====================================================

def download_pajak_pariwisata(request):

    df = pd.DataFrame(

        list(

            PajakPariwisata.objects.all().values(

                "tahun",

                "jenis_pajak",

                "realisasi",

            )

        )

    )

    response = HttpResponse(

        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    response["Content-Disposition"] = (

        'attachment; filename="pajak_pariwisata.xlsx"'

    )

    df.to_excel(

        response,

        index=False,

        engine="openpyxl",

    )

    return response

# =====================================================
# HALAMAN RASIO BELANJA
# =====================================================

def rasio_belanja(request):

    queryset = RasioBelanja.objects.all()

    data = []

    labels = []

    pagu = []

    rasio = []

    for item in queryset:

        data.append({

            "uraian": item.uraian,

            "pagu": item.pagu,

            "rasio": item.rasio,

        })

        labels.append(item.uraian)

        pagu.append(item.pagu)

        rasio.append(item.rasio)

    context = {

        "jumlah_data": queryset.count(),

        "tahun": "2024",

        "jumlah_kategori": queryset.count(),

        "data": data,

        "labels": json.dumps(labels),

        "pagu": json.dumps(pagu),

        "rasio": json.dumps(rasio),

        "api_endpoint": "/api/rasio-belanja/",
        "api_dataset": "Rasio Belanja",

    }

    return render(

        request,

        "dashboard/rasio_belanja.html",

        context,

    )

# =====================================================
# DOWNLOAD RASIO BELANJA
# =====================================================

def download_rasio_belanja(request):

    df = pd.DataFrame(

        list(

            RasioBelanja.objects.all().values(

                "uraian",

                "pagu",

                "rasio",

            )

        )

    )

    response = HttpResponse(

        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    response["Content-Disposition"] = (

        'attachment; filename="rasio_belanja.xlsx"'

    )

    df.to_excel(

        response,

        index=False,

        engine="openpyxl",

    )

    return response

# =====================================================
# HALAMAN REALISASI PERIZINAN
# =====================================================

def realisasi_perizinan(request):

    queryset = RealisasiPerizinan.objects.all()

    data = []

    labels = []

    izin_masuk = []
    izin_terbit = []
    izin_ditolak = []
    dalam_proses = []

    total_masuk = 0
    total_terbit = 0
    total_ditolak = 0
    total_proses = 0

    for item in queryset:

        data.append({

            "nama_izin": item.nama_izin,

            "izin_masuk": item.izin_masuk,

            "izin_terbit": item.izin_terbit,

            "izin_ditolak": item.izin_ditolak,

            "dalam_proses": item.dalam_proses,

        })

        labels.append(item.nama_izin)

        izin_masuk.append(item.izin_masuk)
        izin_terbit.append(item.izin_terbit)
        izin_ditolak.append(item.izin_ditolak)
        dalam_proses.append(item.dalam_proses)

        total_masuk += item.izin_masuk
        total_terbit += item.izin_terbit
        total_ditolak += item.izin_ditolak
        total_proses += item.dalam_proses

    context = {

        "jumlah_data": queryset.count(),

        "jumlah_jenis": queryset.count(),

        "tahun": "2021",

        "data": data,

        "labels": json.dumps(labels),

        "izin_masuk": json.dumps(izin_masuk),

        "izin_terbit": json.dumps(izin_terbit),

        "izin_ditolak": json.dumps(izin_ditolak),

        "dalam_proses": json.dumps(dalam_proses),

        "status_labels": json.dumps([
            "Izin Masuk",
            "Izin Terbit",
            "Izin Ditolak",
            "Dalam Proses",
        ]),

        "status_total": json.dumps([
            total_masuk,
            total_terbit,
            total_ditolak,
            total_proses,
        ]),

        "api_endpoint": "/api/realisasi-perizinan/",
        "api_dataset": "Realisasi Perizinan",

    }

    return render(

        request,

        "dashboard/realisasi_perizinan.html",

        context,

    )


# =====================================================
# DOWNLOAD REALISASI PERIZINAN
# =====================================================

def download_realisasi_perizinan(request):

    df = pd.DataFrame(

        list(

            RealisasiPerizinan.objects.all().values(

                "nama_izin",

                "izin_masuk",

                "izin_terbit",

                "izin_ditolak",

                "dalam_proses",

            )

        )

    )

    response = HttpResponse(

        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    response["Content-Disposition"] = (

        'attachment; filename="realisasi_perizinan.xlsx"'

    )

    df.to_excel(

        response,

        index=False,

        engine="openpyxl",

    )

    return response

# =====================================================
# HALAMAN PROYEK INVESTASI
# =====================================================

def proyek_investasi(request):

    queryset = ProyekInvestasi.objects.all()

    data = []

    labels = []

    pma = []
    pmdn = []

    total_pma = 0
    total_pmdn = 0

    for item in queryset:

        data.append({

            "sektor": item.sektor,

            "pma": item.pma,

            "pmdn": item.pmdn,

        })

        labels.append(item.sektor)

        pma.append(item.pma)
        pmdn.append(item.pmdn)

        total_pma += item.pma
        total_pmdn += item.pmdn

    context = {

        "jumlah_data": queryset.count(),

        "jumlah_sektor": queryset.count(),

        "tahun": "2021",

        "data": data,

        "labels": json.dumps(labels),

        "pma": json.dumps(pma),

        "pmdn": json.dumps(pmdn),

        "investasi_labels": json.dumps([
            "PMA",
            "PMDN",
        ]),

        "investasi_total": json.dumps([
            total_pma,
            total_pmdn,
        ]),

        "api_endpoint": "/api/proyek-investasi/",
        "api_dataset": "Proyek Investasi",

    }

    return render(

        request,

        "dashboard/proyek_investasi.html",

        context,

    )


# =====================================================
# DOWNLOAD PROYEK INVESTASI
# =====================================================

def download_proyek_investasi(request):

    df = pd.DataFrame(

        list(

            ProyekInvestasi.objects.all().values(

                "sektor",

                "pma",

                "pmdn",

            )

        )

    )

    response = HttpResponse(

        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    response["Content-Disposition"] = (

        'attachment; filename="proyek_investasi.xlsx"'

    )

    df.to_excel(

        response,

        index=False,

        engine="openpyxl",

    )

    return response

# =====================================================
# HALAMAN REALISASI APBD
# =====================================================

def realisasi_apbd(request):

    queryset = RealisasiAPBD.objects.all()

    data = []

    for item in queryset:

        data.append({

            "jenis_belanja": item.jenis_belanja,

            "tahun_2021": item.tahun_2021,

            "tahun_2022": item.tahun_2022,

        })

    context = {

        "jumlah_data": queryset.count(),

        "jumlah_jenis": queryset.count(),

        "tahun": "2021 - 2022",

        "data": data,

        "labels": json.dumps(
            [x["jenis_belanja"] for x in data]
        ),

        "tahun2021": json.dumps(
            [x["tahun_2021"] for x in data]
        ),

        "tahun2022": json.dumps(
            [x["tahun_2022"] for x in data]
        ),

        "pie_labels": json.dumps(
            [x["jenis_belanja"] for x in data]
        ),

        "pie_data": json.dumps(
            [x["tahun_2022"] for x in data]
        ),

        "api_endpoint": "/api/realisasi-apbd/",

        "api_dataset": "Realisasi APBD",

    }

    return render(

        request,

        "dashboard/realisasi_apbd.html",

        context,

    )

# =====================================================
# DOWNLOAD REALISASI APBD
# =====================================================

def download_realisasi_apbd(request):

    df = queryset_to_excel(

        RealisasiAPBD.objects.all(),

        fields=[

            "jenis_belanja",

            "tahun_2021",

            "tahun_2022",

        ]

    )

    response = HttpResponse(

        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    response["Content-Disposition"] = (

        'attachment; filename="realisasi_apbd.xlsx"'

    )

    df.to_excel(

        response,

        index=False,

        engine="openpyxl",

    )

    return response

# =====================================================
# HALAMAN KATEGORI SOSIAL
# =====================================================

def kategori_sosial(request):

    datasets = [

        {
            "nama": "Jumlah Siswa Miskin Menurut Status dan Kecamatan di Kota Tangerang Selatan",
            "dinas": "Dinas Sosial",
            "tahun": "2020",
            "jumlah": 7,
            "url": reverse("siswa_miskin"),
        },

        {
            "nama": "Jenis Air Minum yang Dikonsumsi Rumah Tangga Menurut Kecamatan di Kota Tangerang Selatan",
            "dinas": "Dinas Sosial",
            "tahun": "2020",
            "jumlah": 7,
            "url": reverse("air_minum"),
        },

        {
            "nama": "Jumlah Kepemilikan Lahan Keluarga Menurut Status dan Kecamatan di Kota Tangerang Selatan",
            "dinas": "Dinas Sosial",
            "tahun": "2020",
            "jumlah": 7,
            "url": reverse("lahan"),
        },

        {
            "nama": "Informasi Status Kesejahteraan Rumah Tangga dan Individu Menurut Kecamatan di Kota Tangerang Selatan",
            "dinas": "Dinas Sosial",
            "tahun": "2020",
            "jumlah": 7,
            "url": reverse("kesejahteraan"),
        },

        {
            "nama": "Jumlah Kepemilikan Rumah Keluarga Menurut Status dan Kecamatan di Kota Tangerang Selatan Tahun",
            "dinas": "Dinas Sosial",
            "tahun": "2020",
            "jumlah": 7,
            "url": reverse("rumah"),
        },

        {
            "nama": "Persentase PPKS dan DTKS Menurut Kecamatan di Kota Tangerang Selatan",
            "dinas": "Dinas Sosial",
            "tahun": "2022",
            "jumlah": 7,
            "url": reverse("ppks_dtks"),
        },

        {
            "nama": "Tabel 4.1 Jumlah Penduduk Per Kecamatan Berdasarkan Jenis Kelamin",
            "dinas": "Disdukcapil",
            "tahun": "2024",
            "jumlah": 8,
            "url": reverse("penduduk_jenis_kelamin"),
        },

        {
            "nama": "Jumlah Penduduk Menurut Usia 60-64 Tahun dan Menurut Kecamatan di Kota Tangerang Selatan",
            "dinas": "Disdukcapil",
            "tahun": "2024",
            "jumlah": 8,
            "url": reverse("usia_60_64"),
        },

        {
            "nama": "Jumlah Penduduk Penyandang Disabilitas Menurut Jenis dan Kecamatan di Kota Tangerang Selatan",
            "dinas": "Disdukcapil",
            "tahun": "2024",
            "jumlah": 7,
            "url": reverse("disabilitas"),
        },

    ]

    return render(
        request,
        "dashboard/kategori_sosial.html",
        {
            "datasets": datasets,
            "total_dataset": len(datasets),
            "total_dinas": 2,
        }
    )

# =====================================================
# HALAMAN KATEGORI EKONOMI
# =====================================================

def kategori_ekonomi(request):

    datasets = [

        {
            "nama": "Jumlah Kelompok Perikanan Budidaya Menurut Jenis dan Kecamatan di Kota Tangerang Selatan",
            "dinas": "DKPPP",
            "tahun": "2022",
            "jumlah": 7,
            "url": reverse("kelompok_perikanan"),
        },

        {
            "nama": "Jumlah UMKM Menurut Kecamatan di Kota Tangerang Selatan",
            "dinas": "Dinas Koperasi & UKM",
            "tahun": "2022",
            "jumlah": 7,
            "url": reverse("umkm"),
        },

        {
            "nama": "Jumlah Koperasi Menurut Jumlah Aset yang Dimiliki di Kota Tangerang Selatan",
            "dinas": "Dinas Koperasi & UKM",
            "tahun": "2022",
            "jumlah": 4,
            "url": reverse("koperasi"),
        },

        {
            "nama": "Rekapitulasi Pajak Daerah Terkait Sektor Pariwisata Menurut Jenis di Kota Tangerang Selatan",
            "dinas": "Bapenda",
            "tahun": "2018-2021",
            "jumlah": 12,
            "url": reverse("pajak_pariwisata"),
        },

        {
            "nama": "Rasio Belanja Perangkat Daerah di Kota Tangerang Selatan",
            "dinas": "BKAD",
            "tahun": "2023",
            "jumlah": 5,
            "url": reverse("rasio_belanja"),
        },

        {
            "nama": "Jumlah Nilai Realisasi APBD Kota Tangerang Selatan Menurut Jenis Belanja",
            "dinas": "BKAD",
            "tahun": "2021-2022",
            "jumlah": 12,
            "url": reverse("realisasi_apbd"),
        },

        {
            "nama": "Jumlah Realisasi Perizinan Menurut Jenis di Kota Tangerang Selatan",
            "dinas": "DPMPTSP",
            "tahun": "2021",
            "jumlah": 13,
            "url": reverse("realisasi_perizinan"),
        },

        {
            "nama": "Jumlah Proyek Investasi PMA dan PMDN Menurut Sektor di Kota Tangerang Selatan",
            "dinas": "DPMPTSP",
            "tahun": "2021",
            "jumlah": 3,
            "url": reverse("proyek_investasi"),
        },

    ]

    return render(
        request,
        "dashboard/kategori_ekonomi.html",
        {
            "datasets": datasets,
            "total_dataset": len(datasets),
            "total_dinas": 5,
        }
    )

# =====================================================
# DOWNLOAD CSV
# =====================================================

def download_csv(request, dataset):

    model_mapping = {
        "siswamiskin": SiswaMiskin,
        "air": AirMinum,
        "kepemilikanlahan": Lahan,
        "kepemilikanrumah": Rumah,
        "statuskesejahteraan": Kesejahteraan,
        "usia6064": PendudukUsia6064,
        "jeniskelamin": PendudukJenisKelamin,
        "penyandangdisabilitas": PenyandangDisabilitas,
        "ppksdtks": PPKSDTKS,

        "perikanan": KelompokPerikanan,
        "jmlhumkm": UMKM,
        "jmlhkoperasi": Koperasi,
        "pajak": PajakPariwisata,
        "rasio": RasioBelanja,
        "perizinan": RealisasiPerizinan,
        "investasi": ProyekInvestasi,
        "apbd": RealisasiAPBD,
    }

    if dataset not in model_mapping:
        return HttpResponse("Dataset tidak ditemukan")

    model = model_mapping[dataset]

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="{dataset}.csv"'

    writer = csv.writer(response)

    fields = [
        field.name
        for field in model._meta.fields
        if (
            field.name not in ["id", "created_at", "updated_at"]
            and not isinstance(field, ForeignKey)
        )
    ]

    writer.writerow(fields)

    for obj in model.objects.all():
        writer.writerow([getattr(obj, field) for field in fields])

    return response
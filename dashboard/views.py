from django.shortcuts import render
from django.http import HttpResponse
import json
import pandas as pd

from .api import (
    get_siswa_miskin,
    get_air_minum,
    get_lahan,
    get_kesejahteraan,
    get_rumah,
)


# =====================================================
# DASHBOARD
# =====================================================

def home(request):

    siswa = get_siswa_miskin()
    rumah = get_rumah()
    lahan = get_lahan()
    sejahtera = get_kesejahteraan()
    air = get_air_minum()

    # =====================================================
    # CHART 1 - SISWA MISKIN
    # =====================================================

    labels = []
    values = []

    for item in siswa:

        kecamatan = item.get("KECAMATAN")
        total = item.get("Grand Total")

        if not kecamatan:
            continue

        labels.append(kecamatan.strip())
        values.append(int(total or 0))

    # =====================================================
    # CHART 2 - KEPEMILIKAN RUMAH
    # =====================================================

    rumah_labels = [
        "Milik Sendiri",
        "Kontrak/Sewa",
        "Lainnya",
        "Bebas Sewa",
        "Dinas",
    ]

    rumah_values = [
        sum(int(x.get("Milik sendiri") or 0) for x in rumah),
        sum(int(x.get("Kontrak/sewa") or 0) for x in rumah),
        sum(int(x.get("Lainnya") or 0) for x in rumah),
        sum(int(x.get("Bebas sewa") or 0) for x in rumah),
        sum(int(x.get("Dinas") or 0) for x in rumah),
    ]

    # =====================================================
    # CHART 3 - KEPEMILIKAN LAHAN
    # =====================================================

    lahan_labels = [
        "Milik Sendiri",
        "Milik Orang Lain",
        "Tanah Negara",
        "Lainnya",
    ]

    lahan_values = [
        sum(int(x.get("Milik sendiri") or 0) for x in lahan),
        sum(int(x.get("Milik orang lain") or 0) for x in lahan),
        sum(int(x.get("Tanah negara") or 0) for x in lahan),
        sum(int(x.get("Lainnya") or 0) for x in lahan),
    ]

    # =====================================================
    # CHART 4 - STATUS KESEJAHTERAAN
    # =====================================================

    sejahtera_labels = []
    laki_values = []
    perempuan_values = []

    for item in sejahtera:

        kecamatan = item.get("KECAMATAN")

        if not kecamatan:
            continue

        sejahtera_labels.append(kecamatan.strip())
        laki_values.append(int(item.get("Laki-laki") or 0))
        perempuan_values.append(int(item.get("Perempuan") or 0))

    # =====================================================
    # CHART 5 - AIR MINUM
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

    air_keys = [
        "Air isi ulang",
        "Air kemasan bermerk",
        "Air sungai/danau/waduk",
        "Lainnya",
        "Leding eceran",
        "Leding meteran",
        "Air hujan",
        "Mata air tak terlindung",
        "Mata air terlindung",
        "Sumur bor/pompa",
        "Sumur tak terlindung",
        "Sumur terlindung",
    ]

    air_values = []

    for key in air_keys:
        air_values.append(
            sum(int(x.get(key) or 0) for x in air)
        )

    # =====================================================
    # CONTEXT
    # =====================================================

    context = {

        "total_dataset": 5,

        "jumlah_siswa": len(siswa),
        "jumlah_rumah": len(rumah),
        "jumlah_lahan": len(lahan),
        "jumlah_sejahtera": len(sejahtera),
        "jumlah_air": len(air),

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
    }

    return render(request, "dashboard/home.html", context)


# =====================================================
# HALAMAN SISWA MISKIN
# =====================================================

def siswa(request):

    raw = get_siswa_miskin()

    data = []

    for item in raw:

        if not isinstance(item, dict):
            continue

        kecamatan = item.get("KECAMATAN")

        if not kecamatan:
            continue

        data.append({

            "kecamatan": kecamatan.strip(),

            "sd": int(item.get("SD/SDLB") or 0),
            "smp": int(item.get("SMP/ SMPLB") or 0),
            "sma": int(item.get("SMA/SMK /SMALB") or 0),
            "aliyah": int(item.get("M Aliyah") or 0),
            "ibtidaiyah": int(item.get("M Ibtidaiyah") or 0),
            "tsanawiyah": int(item.get("M Tsanawiyah") or 0),
            "paket_a": int(item.get("Paket A") or 0),
            "paket_b": int(item.get("Paket B") or 0),
            "paket_c": int(item.get("Paket C") or 0),
            "pt": int(item.get("Perguruan Tinggi") or 0),
            "lainnya": int(item.get("LAINNYA") or 0),
            "total": int(item.get("Grand Total") or 0),

        })

    context = {

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

    }

    return render(request, "dashboard/siswa_miskin.html", context)


# =====================================================
# DOWNLOAD EXCEL
# =====================================================

def download_siswa(request):

    df = pd.DataFrame(get_siswa_miskin())

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = 'attachment; filename="siswa_miskin.xlsx"'

    df.to_excel(
        response,
        index=False,
        engine="openpyxl"
    )

    return response

# =====================================================
# HALAMAN AIR MINUM
# =====================================================

def air_minum(request):

    raw = get_air_minum()

    data = []

    for item in raw:

        kecamatan = item.get("KECAMATAN")

        if not kecamatan:
            continue

        row = {
            "kecamatan": kecamatan.strip(),

            "air_isi": int(item.get("Air isi ulang") or 0),
            "air_kemasan": int(item.get("Air kemasan bermerk") or 0),
            "air_sungai": int(item.get("Air sungai/danau/waduk") or 0),
            "lainnya": int(item.get("Lainnya") or 0),
            "leding_eceran": int(item.get("Leding eceran") or 0),
            "leding_meteran": int(item.get("Leding meteran") or 0),
            "air_hujan": int(item.get("Air hujan") or 0),
            "mata_air_tak": int(item.get("Mata air tak terlindung") or 0),
            "mata_air_ter": int(item.get("Mata air terlindung") or 0),
            "sumur_bor": int(item.get("Sumur bor/pompa") or 0),
            "sumur_tak": int(item.get("Sumur tak terlindung") or 0),
            "sumur_ter": int(item.get("Sumur terlindung") or 0),

            "total": int(item.get("Grand Total") or 0),
        }

        data.append(row)

    context = {

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

    }

    return render(
        request,
        "dashboard/air_minum.html",
        context
    )

def download_air(request):

    df = pd.DataFrame(get_air_minum())

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="air_minum.xlsx"'
    )

    df.to_excel(
        response,
        index=False,
        engine="openpyxl"
    )

    return response

# =====================================================
# HALAMAN KEPEMILIKAN LAHAN
# =====================================================

def lahan(request):

    raw = get_lahan()

    data = []

    for item in raw:

        if not isinstance(item, dict):
            continue

        kecamatan = item.get("KECAMATAN")

        if not kecamatan:
            continue

        data.append({

            "kecamatan": kecamatan.strip(),

            "milik_sendiri": int(item.get("Milik sendiri") or 0),
            "milik_orang_lain": int(item.get("Milik orang lain") or 0),
            "tanah_negara": int(item.get("Tanah negara") or 0),
            "lainnya": int(item.get("Lainnya") or 0),

            "total": int(item.get("Grand Total") or 0),

        })

    context = {

        "data": data,

        "labels": json.dumps([x["kecamatan"] for x in data]),
        "total": json.dumps([x["total"] for x in data]),

        "milik_sendiri": json.dumps(
            [x["milik_sendiri"] for x in data]
        ),

        "milik_orang_lain": json.dumps(
            [x["milik_orang_lain"] for x in data]
        ),

        "tanah_negara": json.dumps(
            [x["tanah_negara"] for x in data]
        ),

        "lainnya": json.dumps(
            [x["lainnya"] for x in data]
        ),

    }

    return render(
        request,
        "dashboard/lahan.html",
        context
    )


# =====================================================
# DOWNLOAD EXCEL LAHAN
# =====================================================

def download_lahan(request):

    df = pd.DataFrame(get_lahan())

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="kepemilikan_lahan.xlsx"'
    )

    df.to_excel(
        response,
        index=False,
        engine="openpyxl"
    )

    return response

# =====================================================
# HALAMAN STATUS KESEJAHTERAAN
# =====================================================

def kesejahteraan(request):

    raw = get_kesejahteraan()

    data = []

    for item in raw:

        if not isinstance(item, dict):
            continue

        kecamatan = item.get("KECAMATAN")

        if not kecamatan:
            continue

        data.append({

            "kecamatan": kecamatan.strip(),

            "laki": int(item.get("Laki-laki") or 0),

            "perempuan": int(item.get("Perempuan") or 0),

            "total": int(item.get("Grand Total") or 0),

        })

    context = {

        "data": data,

        "labels": json.dumps([x["kecamatan"] for x in data]),

        "total": json.dumps([x["total"] for x in data]),

        "laki": json.dumps([x["laki"] for x in data]),

        "perempuan": json.dumps([x["perempuan"] for x in data]),

    }

    return render(
        request,
        "dashboard/kesejahteraan.html",
        context
    )

# =====================================================
# DOWNLOAD STATUS KESEJAHTERAAN
# =====================================================

def download_kesejahteraan(request):

    df = pd.DataFrame(get_kesejahteraan())

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="status_kesejahteraan.xlsx"'
    )

    df.to_excel(
        response,
        index=False,
        engine="openpyxl"
    )

    return response

# =====================================================
# HALAMAN KEPEMILIKAN RUMAH
# =====================================================

def rumah(request):

    raw = get_rumah()

    data = []

    for item in raw:

        if not isinstance(item, dict):
            continue

        kecamatan = item.get("KECAMATAN")

        if not kecamatan:
            continue

        data.append({

            "kecamatan": kecamatan.strip(),

            "milik_sendiri": int(item.get("Milik sendiri") or 0),
            "kontrak": int(item.get("Kontrak/sewa") or 0),
            "bebas_sewa": int(item.get("Bebas sewa") or 0),
            "dinas": int(item.get("Dinas") or 0),
            "lainnya": int(item.get("Lainnya") or 0),

            "total": int(item.get("Grand Total") or 0),

        })

    context = {

        "data": data,

        "labels": json.dumps([x["kecamatan"] for x in data]),

        "total": json.dumps([x["total"] for x in data]),

        "milik_sendiri": json.dumps(
            [x["milik_sendiri"] for x in data]
        ),

        "kontrak": json.dumps(
            [x["kontrak"] for x in data]
        ),

        "bebas_sewa": json.dumps(
            [x["bebas_sewa"] for x in data]
        ),

        "dinas": json.dumps(
            [x["dinas"] for x in data]
        ),

        "lainnya": json.dumps(
            [x["lainnya"] for x in data]
        ),

    }

    return render(
        request,
        "dashboard/rumah.html",
        context
    )

# =====================================================
# DOWNLOAD KEPEMILIKAN RUMAH
# =====================================================

def download_rumah(request):

    df = pd.DataFrame(get_rumah())

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="kepemilikan_rumah.xlsx"'
    )

    df.to_excel(
        response,
        index=False,
        engine="openpyxl"
    )

    return response
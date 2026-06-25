from django.shortcuts import render
import json

from .api import (
    get_siswa_miskin,
    get_air_minum,
    get_lahan,
    get_kesejahteraan,
    get_rumah
)


def home(request):

    siswa = get_siswa_miskin()
    air = get_air_minum()
    lahan = get_lahan()
    sejahtera = get_kesejahteraan()
    rumah = get_rumah()

    print("CONTOH SISWA:")
    print(siswa[0])

    print("CONTOH RUMAH:")
    print(rumah[0])

    print("CONTOH LAHAN:")
    print(lahan[0])

    print("KEY LAHAN:")
    print(lahan[0].keys())

    # =====================================
    # CHART 1 - SISWA MISKIN
    # =====================================

    labels = []
    values = []

    for item in siswa:

        kecamatan = item.get("KECAMATAN")
        total = item.get("Grand Total")

        # Skip data kosong
        if kecamatan is None or total is None:
            continue

        labels.append(kecamatan)
        values.append(int(total))

    # =====================================
    # CHART 2 - KEPEMILIKAN RUMAH
    # =====================================

    milik_sendiri = 0
    kontrak_sewa = 0
    lainnya = 0
    bebas_sewa = 0
    dinas = 0

    for item in rumah:

        milik_sendiri += int(item.get("Milik sendiri") or 0)
        kontrak_sewa += int(item.get("Kontrak/sewa") or 0)
        lainnya += int(item.get("Lainnya") or 0)
        bebas_sewa += int(item.get("Bebas sewa") or 0)
        dinas += int(item.get("Dinas") or 0)

    rumah_labels = [
        "Milik Sendiri",
        "Kontrak/Sewa",
        "Lainnya",
        "Bebas Sewa",
        "Dinas"
    ]

    rumah_values = [
        milik_sendiri,
        kontrak_sewa,
        lainnya,
        bebas_sewa,
        dinas
    ]

    # =====================================
    # CHART 3 - KEPEMILIKAN LAHAN
    # =====================================

    milik_sendiri_lahan = 0
    milik_orang_lain = 0
    tanah_negara = 0
    lainnya_lahan = 0

    for item in lahan:

        milik_sendiri_lahan += int(item["Milik sendiri"] or 0)
        milik_orang_lain += int(item["Milik orang lain"] or 0)
        tanah_negara += int(item["Tanah negara"] or 0)
        lainnya_lahan += int(item["Lainnya"] or 0)

    lahan_labels = [
        "Milik Sendiri",
        "Milik Orang Lain",
        "Tanah Negara",
        "Lainnya"
    ]

    lahan_values = [
        milik_sendiri_lahan,
        milik_orang_lain,
        tanah_negara,
        lainnya_lahan
    ]

    # =====================================
    # CONTEXT
    # =====================================

    context = {

        "total_dataset": 5,

        "jumlah_siswa": len(siswa),
        "jumlah_air": len(air),
        "jumlah_lahan": len(lahan),
        "jumlah_sejahtera": len(sejahtera),
        "jumlah_rumah": len(rumah),

        # Chart Siswa Miskin
        "labels": json.dumps(labels),
        "values": json.dumps(values),

        # Chart Rumah
        "rumah_labels": json.dumps(rumah_labels),
        "rumah_values": json.dumps(rumah_values),
        # Chart Lahan
        "lahan_labels": json.dumps(lahan_labels),
        "lahan_values": json.dumps(lahan_values),
    }

    return render(
        request,
        "dashboard/home.html",
        context
    )
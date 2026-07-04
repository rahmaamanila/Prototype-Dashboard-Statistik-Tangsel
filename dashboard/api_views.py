from django.utils.timezone import now

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
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
    PendudukJenisKelamin,
    PendudukUsia6064,
    PenyandangDisabilitas,
    PPKSDTKS,
    RealisasiAPBD,
    RealisasiPerizinan,
    ProyekInvestasi,
)

from .serializers import (
    SiswaMiskinSerializer,
    AirMinumSerializer,
    LahanSerializer,
    RumahSerializer,
    KesejahteraanSerializer,
    KelompokPerikananSerializer,
    UMKMSerializer,
    KoperasiSerializer,
    PajakPariwisataSerializer,
    RasioBelanjaSerializer,
    PendudukJenisKelaminSerializer,
    PendudukUsia6064Serializer,
    PenyandangDisabilitasSerializer,
    PPKSDTKSSerializer,
    RealisasiAPBDSerializer,
    RealisasiPerizinanSerializer,
    ProyekInvestasiSerializer,
)


# ==========================================================
# RESPONSE UMUM
# ==========================================================

def create_response(dataset_name, serializer):

    return Response({
        "success": True,
        "status": 200,
        "dataset": dataset_name,
        "source": "Database Dashboard Statistik Tangsel",
        "timestamp": now(),
        "jumlah_data": len(serializer.data),
        "data": serializer.data,
    })


# ==========================================================
# API SISWA MISKIN
# ==========================================================

@api_view(["GET"])
def api_siswa(request):

    queryset = SiswaMiskin.objects.all()

    serializer = SiswaMiskinSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Jumlah Siswa Miskin",
        serializer
    )


# ==========================================================
# API AIR MINUM
# ==========================================================

@api_view(["GET"])
def api_air(request):

    queryset = AirMinum.objects.all()

    serializer = AirMinumSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Jenis Air Minum",
        serializer
    )


# ==========================================================
# API KEPEMILIKAN LAHAN
# ==========================================================

@api_view(["GET"])
def api_lahan(request):

    queryset = Lahan.objects.all()

    serializer = LahanSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Kepemilikan Lahan",
        serializer
    )


# ==========================================================
# API KEPEMILIKAN RUMAH
# ==========================================================

@api_view(["GET"])
def api_rumah(request):

    queryset = Rumah.objects.all()

    serializer = RumahSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Kepemilikan Rumah",
        serializer
    )


# ==========================================================
# API STATUS KESEJAHTERAAN
# ==========================================================

@api_view(["GET"])
def api_kesejahteraan(request):

    queryset = Kesejahteraan.objects.all()

    serializer = KesejahteraanSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Status Kesejahteraan",
        serializer
    )

# ==========================================================
# API KELOMPOK PERIKANAN
# ==========================================================

@api_view(["GET"])
def api_kelompok_perikanan(request):

    queryset = KelompokPerikanan.objects.all()

    serializer = KelompokPerikananSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Kelompok Perikanan",
        serializer
    )

# ==========================================================
# API UMKM
# ==========================================================

@api_view(["GET"])
def api_umkm(request):

    queryset = UMKM.objects.all()

    serializer = UMKMSerializer(
        queryset,
        many=True
    )

    return create_response(
        "UMKM",
        serializer
    )

# ==========================================================
# API KOPERASI
# ==========================================================
@api_view(["GET"])
def api_koperasi(request):

    queryset = Koperasi.objects.all()

    serializer = KoperasiSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Koperasi",
        serializer
    )

# ==========================================================
# API PAJAK PARIWISATA
# ==========================================================
@api_view(["GET"])
def api_pajak_pariwisata(request):

    queryset = PajakPariwisata.objects.all()

    serializer = PajakPariwisataSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Pajak Pariwisata",
        serializer
    )

# ==========================================================
# API RASIO BELANJA
# ==========================================================
@api_view(["GET"])
def api_rasio_belanja(request):

    queryset = RasioBelanja.objects.all()

    serializer = RasioBelanjaSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Rasio Belanja",
        serializer
    )

# ==========================================================
# API REALISASI APBD
# ==========================================================
@api_view(["GET"])
def api_realisasi_apbd(request):

    queryset = RealisasiAPBD.objects.all()

    serializer = RealisasiAPBDSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Realisasi APBD",
        serializer
    )

# ==========================================================
# API PENDUDUK JENIS KELAMIN
# ==========================================================

@api_view(["GET"])
def api_penduduk_jenis_kelamin(request):

    queryset = PendudukJenisKelamin.objects.all()

    serializer = PendudukJenisKelaminSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Penduduk Menurut Jenis Kelamin",
        serializer
    )

# ==========================================================
# API PENDUDUK USIA 60-64
# ==========================================================

@api_view(["GET"])
def api_penduduk_usia(request):

    queryset = PendudukUsia6064.objects.all()

    serializer = PendudukUsia6064Serializer(
        queryset,
        many=True
    )

    return create_response(
        "Penduduk Usia 60-64",
        serializer
    )

# ==========================================================
# API PENYANDANG DISABILITAS
# ==========================================================

@api_view(["GET"])
def api_penyandang_disabilitas(request):

    queryset = PenyandangDisabilitas.objects.all()

    serializer = PenyandangDisabilitasSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Penyandang Disabilitas",
        serializer
    )

# ==========================================================
# API PPKS DTKS
# ==========================================================

@api_view(["GET"])
def api_ppks_dtks(request):

    queryset = PPKSDTKS.objects.all()

    serializer = PPKSDTKSSerializer(
        queryset,
        many=True
    )

    return create_response(
        "PPKS DTKS",
        serializer
    )

# ==========================================================
# API REALISASI PERIZINAN
# ==========================================================

@api_view(["GET"])
def api_realisasi_perizinan(request):

    queryset = RealisasiPerizinan.objects.all()

    serializer = RealisasiPerizinanSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Realisasi Perizinan",
        serializer
    )

# ==========================================================
# API PROYEK INVESTASI
# ==========================================================

@api_view(["GET"])
def api_proyek_investasi(request):

    queryset = ProyekInvestasi.objects.all()

    serializer = ProyekInvestasiSerializer(
        queryset,
        many=True
    )

    return create_response(
        "Proyek Investasi PMA PMDN",
        serializer
    )
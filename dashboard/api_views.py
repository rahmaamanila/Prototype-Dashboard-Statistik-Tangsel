from django.utils.timezone import now

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    SiswaMiskin,
    AirMinum,
    Lahan,
    Rumah,
    Kesejahteraan,
)

from .serializers import (
    SiswaMiskinSerializer,
    AirMinumSerializer,
    LahanSerializer,
    RumahSerializer,
    KesejahteraanSerializer,
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
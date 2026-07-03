from rest_framework import serializers

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
)


class SiswaMiskinSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiswaMiskin
        fields = "__all__"


class AirMinumSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirMinum
        fields = "__all__"


class LahanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lahan
        fields = "__all__"


class RumahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rumah
        fields = "__all__"


class KesejahteraanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kesejahteraan
        fields = "__all__"


class KelompokPerikananSerializer(serializers.ModelSerializer):
    class Meta:
        model = KelompokPerikanan
        fields = "__all__"


class UMKMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UMKM
        fields = "__all__"


class KoperasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Koperasi
        fields = "__all__"


class PajakPariwisataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PajakPariwisata
        fields = "__all__"


class RasioBelanjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RasioBelanja
        fields = "__all__"


class PendudukJenisKelaminSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendudukJenisKelamin
        fields = "__all__"


class PendudukUsia6064Serializer(serializers.ModelSerializer):
    class Meta:
        model = PendudukUsia6064
        fields = "__all__"


class PenyandangDisabilitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenyandangDisabilitas
        fields = "__all__"


class PPKSDTKSSerializer(serializers.ModelSerializer):
    class Meta:
        model = PPKSDTKS
        fields = "__all__"
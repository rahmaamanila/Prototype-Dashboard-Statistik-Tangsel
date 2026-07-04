from django.urls import path

from . import views
from . import api_views

urlpatterns = [

    # =====================================================
    # DASHBOARD
    # =====================================================

    path(
        "",
        views.home,
        name="home"
    ),

    # =====================================================
    # HALAMAN DATASET
    # =====================================================

    path(
        "siswa-miskin/",
        views.siswa,
        name="siswa_miskin"
    ),

    path(
        "air-minum/",
        views.air_minum,
        name="air_minum"
    ),

    path(
        "kepemilikan-lahan/",
        views.lahan,
        name="lahan"
    ),

    path(
        "status-kesejahteraan/",
        views.kesejahteraan,
        name="kesejahteraan"
    ),

    path(
        "kepemilikan-rumah/",
        views.rumah,
        name="rumah"
    ),

    path(
        "usia-60-64/",
        views.usia_60_64,
        name="usia_60_64"
    ),

    path(
        "ppks-dtks/",
        views.ppks_dtks,
        name="ppks_dtks"
    ),

    path(
        "penduduk-jenis-kelamin/",
        views.penduduk_jenis_kelamin,
        name="penduduk_jenis_kelamin"
    ),

    path(
        "penyandang-disabilitas/",
        views.disabilitas,
        name="disabilitas"
    ),

    path(
        "kelompok-perikanan/",
        views.kelompok_perikanan,
        name="kelompok_perikanan"
    ),

    path(
        "umkm/",
        views.umkm,
        name="umkm"
    ),

    path(
        "koperasi/",
        views.koperasi,
        name="koperasi"
    ),

    path(
        "pajak-pariwisata/",
        views.pajak_pariwisata,
        name="pajak_pariwisata"
    ),

    path(
        "rasio-belanja/",
        views.rasio_belanja,
        name="rasio_belanja"
    ),

    path(
        "realisasi-perizinan/",
        views.realisasi_perizinan,
        name="realisasi_perizinan",
    ),

    path(
        "proyek-investasi/",
        views.proyek_investasi,
        name="proyek_investasi",
    ),

    # =====================================================
    # DOWNLOAD EXCEL
    # =====================================================

    path(
        "download/siswa/",
        views.download_siswa,
        name="download_siswa"
    ),

    path(
        "download/air-minum/",
        views.download_air,
        name="download_air"
    ),

    path(
        "download/lahan/",
        views.download_lahan,
        name="download_lahan"
    ),

    path(
        "download/kesejahteraan/",
        views.download_kesejahteraan,
        name="download_kesejahteraan"
    ),

    path(
        "download/rumah/",
        views.download_rumah,
        name="download_rumah"
    ),

    path(
        "download/usia-60-64/",
        views.download_usia_60_64,
        name="download_usia_60_64"
    ),

    path(
        "download/ppks-dtks/",
        views.download_ppks_dtks,
        name="download_ppks_dtks"
    ),

    path(
        "download/penduduk-jenis-kelamin/",
        views.download_penduduk_jenis_kelamin,
        name="download_penduduk_jenis_kelamin"
    ),

    path(
        "download/disabilitas/",
        views.download_disabilitas,
        name="download_disabilitas"
    ),

    path(
        "download/kelompok-perikanan/",
        views.download_kelompok_perikanan,
        name="download_kelompok_perikanan"
    ),

    path(
        "download/umkm/",
        views.download_umkm,
        name="download_umkm"
    ),

    path(
        "download/koperasi/",
        views.download_koperasi,
        name="download_koperasi"
    ),

    path(
        "download/pajak-pariwisata/",
        views.download_pajak_pariwisata,
        name="download_pajak_pariwisata"
    ),

    path(
        "download/rasio-belanja/",
        views.download_rasio_belanja,
        name="download_rasio_belanja"
    ),

    path(
        "download/realisasi-perizinan/",
        views.download_realisasi_perizinan,
        name="download_realisasi_perizinan",
    ),

    path(
        "download/proyek-investasi/",
        views.download_proyek_investasi,
        name="download_proyek_investasi",
    ),

    # =====================================================
    # REST API DASHBOARD
    # =====================================================

    path(
        "api/siswa-miskin/",
        api_views.api_siswa,
        name="api_siswa"
    ),

    path(
        "api/air-minum/",
        api_views.api_air,
        name="api_air"
    ),

    path(
        "api/kepemilikan-lahan/",
        api_views.api_lahan,
        name="api_lahan"
    ),

    path(
        "api/status-kesejahteraan/",
        api_views.api_kesejahteraan,
        name="api_kesejahteraan"
    ),

    path(
        "api/kepemilikan-rumah/",
        api_views.api_rumah,
        name="api_rumah"
    ),

    path(
        "api/kelompok-perikanan/",
        api_views.api_kelompok_perikanan,
        name="api_kelompok_perikanan",
    ),

    path(
        "api/umkm/",
        api_views.api_umkm,
        name="api_umkm",
    ),

    path(
        "api/koperasi/",
        api_views.api_koperasi,
        name="api_koperasi",
    ),

    path(
        "api/pajak-pariwisata/",
        api_views.api_pajak_pariwisata,
        name="api_pajak_pariwisata",
    ),

    path(
        "api/rasio-belanja/",
        api_views.api_rasio_belanja,
        name="api_rasio_belanja",
    ),

    path(
        "api/realisasi-apbd/",
        api_views.api_realisasi_apbd,
        name="api_realisasi_apbd",
    ),

    path(
        "api/penduduk-jenis-kelamin/",
        api_views.api_penduduk_jenis_kelamin,
        name="api_penduduk_jenis_kelamin",
    ),

    path(
        "api/penduduk-usia/",
        api_views.api_penduduk_usia,
        name="api_penduduk_usia",
    ),

    path(
        "api/penyandang-disabilitas/",
        api_views.api_penyandang_disabilitas,
        name="api_penyandang_disabilitas",
    ),

    path(
        "api/ppks-dtks/",
        api_views.api_ppks_dtks,
        name="api_ppks_dtks",
    ),

    path(
        "api/realisasi-perizinan/",
        api_views.api_realisasi_perizinan,
        name="api_realisasi_perizinan",
    ),

    path(
        "api/proyek-investasi/",
        api_views.api_proyek_investasi,
        name="api_proyek_investasi",
    ),

]
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ==========================================================
# KONFIGURASI SESSION REQUEST
# ==========================================================

session = requests.Session()

retry = Retry(
    total=3,
    connect=3,
    read=3,
    backoff_factor=1,
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retry)

session.mount("https://", adapter)
session.mount("http://", adapter)


# ==========================================================
# BASE URL PORTAL DATA TANGSEL
# ==========================================================

BASE_URL = "https://data.tangerangselatankota.go.id/api/3/action/datastore_search"


# ==========================================================
# RESOURCE ID DATASET
# ==========================================================

RESOURCE_IDS = {

    # ==========================
    # SOSIAL
    # ==========================

    "siswa_miskin": "a8849840-a3d8-43da-bd19-43d7434d1e85",

    "air_minum": "d49eb4e7-b637-4894-a54e-f9df01ff6965",

    "lahan": "283549a1-538d-4ac5-9612-89844d6a9a63",

    "kesejahteraan": "acae6558-61bc-4db5-b2e8-b730dcd162db",

    "rumah": "8d41bae6-ddad-46da-b5cd-30fe3dede398",

    # ==========================
    # EKONOMI
    # ==========================

    "kelompok_perikanan": "4b465cad-a74a-4636-be0f-9ace62e6e96a",

    "umkm": "8f2ccd29-7b84-45df-ab71-fedd4919f0de",

    "koperasi": "2314307f-f866-4f41-8954-48d5e6635299",

    "pajak_pariwisata": "ac40f298-2f14-4e42-8219-8ffcf0bd900a",

    "rasio_belanja": "46d31bc5-bd52-4e52-a5d9-1a8977f3d544",

    # ==========================
    # DATASET TAMBAHAN
    # ==========================

    "penduduk_jenis_kelamin": "e0d44b13-c1a8-411f-8469-1dedff7deedc",

    "penyandang_disabilitas": "78e1c90a-1185-47f0-a26f-139e6367acbf",

    "realisasi_perizinan": "839273fa-b94f-4a75-9527-fccc1e1a401c",

    "proyek_investasi": "8dd92643-2ffe-4860-9a8c-bdde7ce9d04c",
}


# ==========================================================
# REQUEST DATA UMUM
# ==========================================================

def fetch_data(resource_id, limit=1000):

    url = f"{BASE_URL}?resource_id={resource_id}&limit={limit}"

    try:

        response = session.get(
            url,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        if data.get("success"):

            return data["result"]["records"]

    except requests.exceptions.SSLError as e:
        print("SSL Error :", e)

    except requests.exceptions.ConnectionError as e:
        print("Connection Error :", e)

    except requests.exceptions.Timeout as e:
        print("Timeout :", e)

    except requests.exceptions.RequestException as e:
        print("Request Error :", e)

    except Exception as e:
        print("Unexpected Error :", e)

    return []


# ==========================================================
# REQUEST METADATA
# ==========================================================

def fetch_dataset_info(resource_id):

    url = f"{BASE_URL}?resource_id={resource_id}&limit=1"

    try:

        response = session.get(url, timeout=20)

        response.raise_for_status()

        data = response.json()

        if data.get("success"):

            return data["result"]

    except Exception as e:

        print("Metadata Error :", e)

    return None


# ==========================================================
# FUNGSI SETIAP DATASET
# ==========================================================

def get_siswa_miskin():
    return fetch_data(RESOURCE_IDS["siswa_miskin"])


def get_air_minum():
    return fetch_data(RESOURCE_IDS["air_minum"])


def get_lahan():
    return fetch_data(RESOURCE_IDS["lahan"])


def get_kesejahteraan():
    return fetch_data(RESOURCE_IDS["kesejahteraan"])


def get_rumah():
    return fetch_data(RESOURCE_IDS["rumah"])


def get_kelompok_perikanan():
    return fetch_data(RESOURCE_IDS["kelompok_perikanan"])


def get_umkm():
    return fetch_data(RESOURCE_IDS["umkm"])


def get_koperasi():
    return fetch_data(RESOURCE_IDS["koperasi"])


def get_pajak_pariwisata():
    return fetch_data(RESOURCE_IDS["pajak_pariwisata"])


def get_rasio_belanja():
    return fetch_data(RESOURCE_IDS["rasio_belanja"])


def get_realisasi_perizinan():
    return fetch_data(
        RESOURCE_IDS["realisasi_perizinan"]
    )

def get_proyek_investasi():
    return fetch_data(
        RESOURCE_IDS["proyek_investasi"]
    )


# ==========================================================
# CEK STATUS API
# ==========================================================

def check_api_status():

    url = "https://data.tangerangselatankota.go.id/api/3/action/package_list"

    try:

        response = session.get(url, timeout=5)

        if response.status_code == 200:

            return {
                "status": "Online",
                "badge": "success",
                "icon": "fa-check-circle"
            }

    except Exception:
        pass

    return {
        "status": "Offline",
        "badge": "danger",
        "icon": "fa-times-circle"
    }

# ===========================================
# PENDUDUK BERDASARKAN JENIS KELAMIN
# ===========================================

def get_penduduk_jenis_kelamin():
    return fetch_data(
        RESOURCE_IDS["penduduk_jenis_kelamin"]
    )


# ===========================================
# PENYANDANG DISABILITAS
# ===========================================

def get_penyandang_disabilitas():
    return fetch_data(
        RESOURCE_IDS["penyandang_disabilitas"]
    )
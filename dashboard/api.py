import requests


def get_siswa_miskin():

    url = "https://data.tangerangselatankota.go.id/api/3/action/datastore_search?resource_id=a8849840-a3d8-43da-bd19-43d7434d1e85"

    response = requests.get(url)
    data = response.json()

    return data["result"]["records"]


def get_air_minum():

    url = "https://data.tangerangselatankota.go.id/api/3/action/datastore_search?resource_id=d49eb4e7-b637-4894-a54e-f9df01ff6965"

    response = requests.get(url)
    data = response.json()

    return data["result"]["records"]


def get_lahan():

    url = "https://data.tangerangselatankota.go.id/api/3/action/datastore_search?resource_id=283549a1-538d-4ac5-9612-89844d6a9a63"

    response = requests.get(url)
    data = response.json()

    return data["result"]["records"]


def get_kesejahteraan():

    url = "https://data.tangerangselatankota.go.id/api/3/action/datastore_search?resource_id=acae6558-61bc-4db5-b2e8-b730dcd162db"

    response = requests.get(url)
    data = response.json()

    return data["result"]["records"]


def get_rumah():

    url = "https://data.tangerangselatankota.go.id/api/3/action/datastore_search?resource_id=8d41bae6-ddad-46da-b5cd-30fe3dede398"

    response = requests.get(url)
    data = response.json()

    return data["result"]["records"]
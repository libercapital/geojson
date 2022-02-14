import requests
import json


def main():
    print("Making request to ibge to get GeoJson..")
    ibge_request = requests.get(
        "https://servicodados.ibge.gov.br/api/v3/malhas/paises/BR?intrarregiao=UF&formato=application/vnd.geo+json"
    )

    if ibge_request.status_code != 200:
        print(f"Error to make request. Reason: {ibge_request.reason}")
        exit()

    print("Getting GeoJson result..")
    json_ibge = ibge_request.json()

    if len(json_ibge) == 0:
        print(f"Error: Empty json!")
        exit()

    print("Loading state mapping..")
    with open('mapping.json', 'r') as f:
        mapping = json.load(f)

    print("Making state mapping..")
    for f in json_ibge['features']:
        f['properties'].update(mapping[f['properties']['codarea']])

    print("Saving brazilian_states.json..")
    with open('brazilian_states.json', 'w') as f:
        json.dump(json_ibge, f)

    print("End")


if __name__ == "__main__":
    main()

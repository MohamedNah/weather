import requests


def get_data(place, period=None, type_data=None):
    url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

    querystring = {"aggregateHours": "24", "location": f"{place}",
                   "contentType": "json", "unitGroup": "metric",
                   "shortColumnNames": "0"}

    headers = {
        "X-RapidAPI-Key": "11109a1ad0mshab570cee9731968p16e92djsn766bdb255270",
        "X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()['locations'][f'{place}']['values'][:int(period)]

    requested_dates = []

    for row in data:
        requested_dates.append(row['datetimeStr'][:10])

    requested_data = []

    if type_data == 'Temperature':
        for row in data:
            requested_data.append(row['temp'])
    else:
        for row in data:
            requested_data.append(row['conditions'])

    return requested_dates, requested_data


if __name__ == '__main__':
    print(get_data('Nouakchott', 5, "Temperature"))


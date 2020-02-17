from urllib.request import urlopen
import json

# with open("data.json") as file:
#     data = json.load(file)
#
# with open("people.json", "w") as dumper:
#     dump_data = json.dump(data, dumper, ensure_ascii=True, indent=4, separators=[":", ","])


#############################################################################################
# API CALL
API_KEY = "f57f78b88df782edef2d267985a11166"  # insert your own API key!!!


def get_weather_data(api_key, location="Barcelona,ES", metric=True):
    unit_system = "metrics" if metric is True else "imperial"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'
    response = urlopen(url.format(location, unit_system, api_key)).read()
    data = json.loads(response)

    # echo the data
    for key, val in data.items():
        print(key, val)
    #
    return data


#############################################################################################
# RUN
if __name__ == '__main__':
    weather_data = get_weather_data(api_key=API_KEY, location="Manchester,UK", metric=False)

    # output specific info
    print(weather_data["coord"])
    print(weather_data["weather"])

"""
this Program downloads a json file from "https://idph.illinois.gov/DPHPublicInformation/api/COVIDExport/GetIllinoisCases" and can create two different
charts for number of exposed cases in Illinois and a the second one for number of deaths in Illinois
"""
import json
import datetime
from urllib.request import urlopen
import matplotlib
import matplotlib.pyplot as plot

URL = "https://idph.illinois.gov/DPHPublicInformation/api/COVIDExport/GetIllinoisCases"


def main():
    print("Downloading file from www.idph.illinois.gov plaese wait for a second......")
    dataset = urlopen(URL)
    json_data = json.loads(dataset.read())
    user_input = input("Enter 1 to create exposed cases chart,Enter 2 to create Deaths chart: ")
    while True:
        if user_input == "1":
            create_exposed_chart(json_data)
            print("chart has been  created successfully in project directory")
            break
        elif user_input=="2":
            create_confirmed_death_chart(json_data)
            print("chart has been  created successfully in project directory")
            break
        else:
            user_input = input("Enter 1 to create exposed cases chart,Enter 2 to create Deaths chart: ")
def create_exposed_chart(json_data):
    cases = {}
    for item in json_data:
        Date = item['testDate']
        # reformat Date
        processed_data = get_date(Date)
        cases[processed_data] = item['confirmed_cases']
    plot_for_confirmed_cases(cases,create_chart_for="confirmed_cases")

def create_confirmed_death_chart(json_data):
    cases = {}
    for item in json_data:
        Date = item['testDate']
        # reformat Date
        processed_date = get_date(Date)
        cases[processed_date] = item['deaths']
    plot_for_confirmed_cases(cases, create_chart_for="deaths")

def plot_for_confirmed_cases(cases,create_chart_for):
    # turn number of cases into a list
    counts = []
    # loop over the dates
    for item in cases:
        counts.append(cases[item])
    x = matplotlib.dates.date2num(list(cases.keys()))
    y = counts
    if create_chart_for == "confirmed_cases":
        matplotlib.pyplot.plot_date(x, y, color="b")
        plot.savefig("confirmed_cases.png")
    else:
        matplotlib.pyplot.plot_date(x, y, color="r")

        plot.savefig("confirmed_deaths.png")

def get_date(time_string):
    # This method converts "2020-03-10T00:00:00" to "2020-03-10" Format
    date_time_obj = datetime.datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%S')
    return date_time_obj.date()


if __name__ == '__main__':
    main()

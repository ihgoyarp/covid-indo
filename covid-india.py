# importing modules
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

# storing the url in the form of string
url = "https://api.covid19india.org/state_district_wise.json"

# function to get data from api


def casesData():
    # getting the json data by calling api
    data = ((requests.get(url)).json())
    states = []

    # getting states
    for key in data.items():
        states.append(key[0])

    # getting statewise data
    for state in states:
        f = (data[state]['districtData'])
        tc = []
        dis = []
        act, con, dea, rec = 0, 0, 0, 0

        # getting districtwise data
        for key in (data[state]['districtData']).items():
            district = key[0]
            dis.append(district)
            active = data[state]['districtData'][district]['active']
            confirmed = data[state]['districtData'][district]['confirmed']
            if district == 'Unknown':
                active, confirmed
            tc.append([active, confirmed])
            act = act + active
            con = con + confirmed
        tc.append([act, con])
        dis.append('Total')
        parameters = ['Active', 'Confirmed']

        # creating a dataframe
        df = pd.DataFrame(tc, dis, parameters)
        print('COVID - 19', state, 'District Wise Data')
        print(df)

        # plotting of data
        plt.bar(dis, df['Active'], width=0.5, align='center')
        fig = plt.gcf()
        fig.set_size_inches(18.5, 10.5)
        plt.xticks(rotation=75)
        plt.show()
        print('*' * 100)


casesData()

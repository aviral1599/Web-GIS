
import random
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt
import requests

sns.set_style('whitegrid')

def plotting():
    url = 'http://127.0.0.1:3000/api'
    r = requests.get(url)
    df = pd.read_json(r.text)
    print(df)
    # print(df)

    fp = "Application\GIS\Indian_States.shp"
    map_df = gpd.read_file(fp)
    print(map_df.head())


    map_df.plot()

    merged = map_df.set_index('st_nm').join(df.set_index('State'))
    print(merged.head())

    # fig, ax = plt.subplots(1, figsize=(10, 6))
    # ax.axis('off')
    # ax.set_title('State Wise Crime', fontdict={'fontsize': '25', 'fontweight' : '3'})

    # plot the figure
    # merged.plot(column='Theft', cmap='YlGn', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    # plt.savefig('mgis2.png')
    # plt.show()
    return merged
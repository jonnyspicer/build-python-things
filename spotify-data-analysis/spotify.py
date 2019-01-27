import json
import pandas as pd
import datetime
import pandas_datareader.data as web
# import matplotlib.pyplot as plt
# from matplotlib import style
from pandas.io.json import json_normalize
from pprint import pprint

# style.use('fivethirtyeight')

with open('data.json') as f:
    data = json.load(f)
    json_normalize(data)
    data = pd.DataFrame.from_dict(data['songs'], orient='columns')
    data.reset_index(level=0, inplace=True)
    print(data)

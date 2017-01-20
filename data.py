import pandas as pd
import pickle
reader = pd.read_csv('data.txt',header=None,iterator=True)
keys = [20170110,20170109,20170108,20170107]
d = {}
data = reader.get_chunk(20000000)
del data[3]
del data[2]
groupby = data.groupby(1)
for key in keys:
    five_date_before_id = []
    for i in range(1,6):
        five_date_before_id = five_date_before_id + groupby.get_group(key-i)[0].values.tolist()
    d[key] = list(set(groupby.get_group(key)[0].values.tolist()).difference(set(five_date_before_id)))
output = open('myfile.pkl', 'wb')
pickle.dump(d, output)
output.close()

import pandas as pd
data = pd.read_csv('Harris.csv')
for dat in data['ID']:
    if 'NGC 104' in dat:
        print("True")
    else:
        print("NO")    
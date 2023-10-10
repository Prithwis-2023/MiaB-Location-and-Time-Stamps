import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy import constants as const
import pandas as pd
from csv import writer

df = pd.read_csv("timestamp.csv")
#df1 = pd.read_csv("timestamp_refined.csv")

headers = []
for header in df:
    headers.append(header)

print(len(df))
print(headers)
print("------------------------")
for i in range(len(df)):
    ls = []
    for header in headers:
        elements = df[header]
        ls.append(elements[i])
    
    rsun_with_error = ls[5].split("   ")    
    ls.pop(5)
    ls.insert(5, rsun_with_error[0])
    ls.insert(6, rsun_with_error[1])
    
    rgc_with_rv = ls[7].split(" ")
    rgc_with_rv2 = [ele for ele in rgc_with_rv if ele != '']
    ls.pop(7)
    ls.insert(7, rgc_with_rv[0])
    ls.insert(8, rgc_with_rv[1])
    
    #print(ls)
    #print(len(ls))
    #print("-----------------------")
    with open('timestamp_refined.csv', 'a') as f_object:
 
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(ls)

        # Close the file object
        f_object.close()



'''
for elements in df["Rsun  ERsun"]:
    ls = []
    elements = str(elements).split('  ')
    RSun = elements[0]
    ERsun = elements[1]
'''    
import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy import constants as const
import pandas as pd
from csv import writer
import math
from math import *

df = pd.read_csv("timestamp.csv")

headers = []
for header in df:
    headers.append(header)

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
    ls.insert(7, rgc_with_rv2[0])
    ls.insert(8, rgc_with_rv2[1])
    
    mualpha = ls[10].split(" ")
    mualpha2 = [ele for ele in mualpha if ele != '']
    ls.pop(10)
    ls.insert(10, mualpha2[0])
    ls.insert(11, mualpha2[1])

    mu_delta_rhopmrade = ls[12].split(" ")
    mu_delta_rhopmrade2 = [ele for ele in mu_delta_rhopmrade if ele != '']
    ls.pop(12)
    ls.insert(12, mu_delta_rhopmrade2[0])
    ls.insert(13, mu_delta_rhopmrade2[1])
    ls.insert(14, mu_delta_rhopmrade2[2])

    r_peri = ls[27].split(" ")
    r_peri2 = [ele for ele in r_peri if ele != '']
    ls.pop(27)
    ls.insert(27, r_peri2[0])
    ls.insert(28, r_peri2[1])

    r_apo = ls[29].split(" ")
    r_apo2 = [ele for ele in r_apo if ele != '']
    ls.pop(29)
    ls.insert(29, r_apo2[0])
    ls.insert(30, r_apo2[1])

    v = math.sqrt(float(ls[21])**2 + float(ls[23])**2 + float(ls[25])**2)
    e_v = math.sqrt(((float(ls[21]) / v) * float(ls[22]))**2 + ((float(ls[23]) / v) * float(ls[24]))**2 + ((float(ls[25]) / v) * float(ls[26]))**2)
    ls.insert(31, v)
    ls.insert(32, e_v)

    with open('timestamp_refined.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(ls)
        f_object.close()


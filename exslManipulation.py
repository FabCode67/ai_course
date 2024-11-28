import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print ("MatolotLib version: ", mp.__version__)


data = pd.read_excel("C:\\Users\\fab\\Documents\\projects\\aicourse\\Canada.xlsx", skiprows=range(20), skipfooter=2, sheet_name='Canada by Citizenship', engine='openpyxl')

data.head()
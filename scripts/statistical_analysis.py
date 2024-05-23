import pandas as pd
import statsmodels.api as sm
from scipy.stats import kendalltau

file = 'Datasetappleton.csv'
df = pd.read_csv(file)

SWL = df['Surface water levels (m)']
TP = df['Total Precipitation (mm)']

#Computing kendall tau coefficient due to large amount of datapoints
tau, p_value = kendalltau(TP, SWL)
print("Kendall's Tau:", tau)
print("P-value:", p_value)

x = sm.add_constant(SWL)
model = sm.OLS(TP, x).fit()
print(model.summary())

#Due to a very low Kendall's Tau, p-value and r squared value, the two variables (precipitation, surface water levels) have a very minor relationship if any at all.
#This means that this body of water recharges MOSTLY from other sources (ex: groundwater), and not from precipitation
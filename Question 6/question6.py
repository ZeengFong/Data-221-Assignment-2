import pandas as pd

crime_df = pd.read_csv('crime.csv')
crime_df['risk'] = crime_df['ViolentCrimesPerPop'].apply(lambda x: "HighCrime" if x >= 0.50 else "LowCrime")
unemployment_by_crime_rate = crime_df.groupby('risk')['PctUnemployed'].mean()
print(f"The unemployment rate in high crime areas is {round(unemployment_by_crime_rate['HighCrime'],2)}")
print(f"The unemployment rate in low crime areas is {round(unemployment_by_crime_rate['LowCrime'],2)}")
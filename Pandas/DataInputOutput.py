import pandas as pd

#Reading from an HTML

data = pd.read_html('https://www.fdic.gov/Bank/individual/failed/banklist.html')
print(data[0].head())


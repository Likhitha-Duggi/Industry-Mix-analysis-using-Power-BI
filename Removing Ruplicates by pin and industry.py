import pandas as pd

# load the data into a pandas dataframe
data = pd.read_excel(r'D:\USF SEM 2\EIS\Group Project\Business Tax ID Data 2015.xlsx')

# Remove duplicates based on PIN # and Industry
data = data.drop_duplicates(subset=["PIN #", "Industry"], keep="first")

# Write the output to a CSV file
data.to_csv("2015output.csv", index=False)

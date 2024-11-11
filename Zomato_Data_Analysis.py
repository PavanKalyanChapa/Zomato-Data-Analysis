import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

dataframe = pd.read_csv("Zomato data .csv")
print(dataframe.head())

def handlerate(value):
  value = str(value).split("/")
  value = value[0]
  return float(value)

dataframe["rate"] = dataframe["rate"].apply(handlerate)
print(dataframe["rate"])

# Displays the count of null values in each column
print(dataframe.isnull().sum())

sb.countplot(x=dataframe['listed_in(type)'],palette='viridis')
plt.xlabel("Type of Restarunt")
plt.ylabel("Count")
plt.show()

grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes':grouped_data})
plt.plot(result, c = "#FFDB58" , marker = 'o' )
plt.xlabel("Type of Restarunt", c = "green" ,size = 20)
plt.ylabel("Votes" , c = "green" , size = 20)

for x, y in enumerate(result['votes']):
    plt.text(x, y, str(y), color="black", ha="left", va="bottom", fontsize=10)

max_votes = dataframe['votes'].max()
restarunt_with_maxvotes = dataframe.loc[dataframe['votes'] == max_votes,'name']

print("Restaurant(s) with the maximum votes:")
print(restarunt_with_maxvotes)

sb.countplot(x=dataframe['online_order'],palette='viridis')
plt.xlabel("Online Order")
plt.show()

plt.hist(dataframe['rate'],bins = 5)
plt.xlabel("Rating")
plt.show()

sb.countplot(x=dataframe['approx_cost(for two people)'],palette = 'viridis')

plt.show()

plt.figure(figsize=(6,6))
sb.boxplot(x = 'online_order', y = 'rate', data = dataframe,palette='viridis')
plt.show()

pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sb.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()

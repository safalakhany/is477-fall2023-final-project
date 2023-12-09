import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import ssl

car_df = pd.read_csv('data/cardata.csv')


plt.figure(figsize=(10, 6))
car_df['buying'].value_counts().plot(kind='bar', color='skyblue', alpha=0.7)
plt.title('Distribution of Buying Price Categories')
plt.xlabel('Buying Price')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

plt.savefig('results/buying_price.png')
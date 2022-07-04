#import modules
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

#read dataset
my_data = pd.read_csv('assignment_seven.csv', sep=',')
#remove real name from dataset
my_data.drop("full_name", axis=1, inplace=True)
#missing entry for any field in a given row, remove that row
my_data.dropna(axis=0, how="any", inplace=True)


#Output a new dataset file
my_data.to_csv('output.csv', sep=',', index=False)

#the top five products that customers bought
df = my_data['products']
product_counts= {}
for word in df:
	try:
		product_counts[word]+=1
	except:
		product_counts[word]=1
    
Counter = Counter(product_counts)

most_products = Counter.most_common(5)
print(most_products)

#create a visualization of the ranking
# ranked 1 to 5 from left to right
x = []
y = []
for i in most_products:
  x.append(i[0])

for j in most_products:
  y.append(j[1])


plt.bar(x, y, color = ['red', 'green'])
# naming the x axis
plt.xlabel('Product Name')
# naming the y axis
plt.ylabel('Number of products sold')
  
# giving a title to my graph
plt.title('Top Five Products')
  
# function to show the bar
plt.show()


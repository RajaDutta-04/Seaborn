import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = {
    "Mobile":["Samsung","Apple","Nokia","Vivo"],
    "Sales":[100,20,50,80]
}

df = pd.DataFrame(data)

sns.barplot(x="Mobile",y="Sales",data=df,palette="viridis")
plt.title("Mobile Sales")
plt.xlabel("Mobile Companies")
plt.ylabel("Sales")
plt.show()

"""
Parametres : -- 

hue , palette , color - same as lineplot

estimator - Choose the statistic (mean, median, etc.)
order - Specify the order of categories
"""

#Use of estimator

data = {
    "Mobile":["Samsung","Apple","Nokia","Vivo","Samsung","Nokia"],
    "Sales":[100,20,50,80,90,30]
}

df = pd.DataFrame(data)

sns.barplot(x="Mobile",y="Sales",data=df,estimator=np.mean) #Samsung has multiple value ==> calculate mean to plot
plt.title("Mobile Sales")
plt.xlabel("Mobile Companies")
plt.ylabel("Sales")
plt.show()

"""
estimator values:

1. np.mean - default
2. np.median
3. np.max
4. np.min
"""

# Use of Order
sns.barplot(x="Mobile",y="Sales",data=df,estimator=np.mean,order=["Nokia","Apple","Samsung","Vivo"],errorbar=None) #Samsung has multiple value ==> calculate mean to plot
plt.title("Mobile Sales")
plt.xlabel("Mobile Companies")
plt.ylabel("Sales")
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Gender":["Male","Female","Female","Male","Female","Trans","Male","Trans"]
}

df = pd.DataFrame(data)


# sns.countplot(x="Gender",data=df,palette="viridis") #plots bar on x-axis
# plt.show()

# sns.countplot(y="Gender",data=df,palette="viridis") #plots bar on y-axis
# plt.show()

"""
Parametres
1. hue , color , palette , order

**2. stat = "count" (default) / "percent" / "proportion"
"""

sns.countplot(y="Gender",data=df,palette="viridis",stat = "percent") 
plt.show()
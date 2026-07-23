"""
catplot() is a figure-level function in Seaborn used to visualize categorical data.

Think of it as a wrapper around several categorical plots.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Height" : [5.1,5.3,6.1,6.5,4.2,5.9,6.0,5.5],
    "Weight" : [70,68,62,60,75,61,63,66],
    "Age" : [20,22,25,28,12,15,17,13]
}

df = pd.DataFrame(data)


"""
Parametres:

1. kind : "strip" --> dots that may overlap
          "swarm" --> same as strip but no overlapping
          "box" --> same as boxplot
          "violin" --> same as violin plot
          "boxen" --> Shows more quantiles than boxplot
          "bar" --> same as bar plot
          "count" --> same as count plot
2. hue , palette , height
"""

#strip
sns.catplot(data=df,kind="strip")
plt.show()

#swarm 
sns.catplot(data=df,kind="swarm")
plt.show()

#violin
sns.catplot(data=df,kind="violin")
plt.show()

#boxen
sns.catplot(data=df,kind="boxen")
plt.show()
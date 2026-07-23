"""
A pair plot is one of Seaborn's most powerful visualization tools. It lets you explore relationships between multiple numerical variables at the same time.

Instead of creating many scatter plots manually, pairplot() creates all possible pairwise scatter plots in a single figure.

It also shows the distribution of each variable on the diagonal.
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
1. vars - Plots only selected variables.
    vars = ["Height","Gender"]

    x_vars - Choose variables only for the x-axis.
    y_vars - Choose variables only for the x=y-axis.
"""

sns.pairplot(df,x_vars=["Height","Age"],y_vars=["Weight"])
plt.show()
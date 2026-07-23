import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Gender":["Male","Female","Female","Male","Male","Male","Male","Female","Female","Male","Female","Female"],
    "Meal":["dinner","lunch","dinner","dinner","lunch","lunch","dinner","dinner","dinner","lunch","dinner","dinner"]
}

df = pd.DataFrame(data)
g = sns.FacetGrid(data=df , col = "Gender")
g.map_dataframe(sns.countplot,x="Meal")
plt.show()

"""
Parametres:

1. row : Creates multiple plots vertically.
2. col: Creates multiple plots horizontally.
3. col_wrap : Wraps the columns into multiple rows. (Useful when there are many categories)
4. sharex : "True" --> if the plots share same x-axis.
            "False" --> if the plots don't share same x-axis.
5. sharey : "True" --> if the plots share same y-axis.
            "False" --> if the plots don't share same y-axis.
"""
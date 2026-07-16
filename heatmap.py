import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = {
    "Raja":[90,80,70,100],
    "Rupak":[80,30,40,95],
    "Ayush":[50,85,95,25]
}

df = pd.DataFrame(data)

sns.heatmap(df)
plt.yticks([0.5,1.5,2.5,3.5],["Physics","Chemistry","Math","Biology"])
plt.show()

"""
Parametres:

"""

#annot - Shows the actual number , fmt - controls how the numbers are displayed
"""
fmt = "d" , "0.1f" , "0.2f" , "0.3f"
"""
sns.heatmap(df,annot=True,fmt="d")
plt.yticks([0.5,1.5,2.5,3.5],["Physics","Chemistry","Math","Biology"])
plt.show()


"""
| cmap     | Description             |
| -------- | ----------------------- |
| Blues    | Light → Dark Blue       |
| Reds     | Light → Dark Red        |
| Greens   | Green shades            |
| Oranges  | Orange shades           |
| Purples  | Purple shades           |
| coolwarm | Blue → Red              |
| viridis  | Purple → Green → Yellow |
| magma    | Black → Orange          |
| inferno  | Black → Yellow          |
| cividis  | Colorblind-friendly     |

"""

sns.heatmap(df,annot=True,fmt="d",cmap="cividis")
plt.yticks([0.5,1.5,2.5,3.5],["Physics","Chemistry","Math","Biology"])
plt.show()

#linewidth- Adds border between cells , linecolor - Color of border
sns.heatmap(df,annot=True,fmt="d",cmap="cividis",linewidths=1,linecolor="black")
plt.yticks([0.5,1.5,2.5,3.5],["Physics","Chemistry","Math","Biology"])
plt.show()

"""
For data cleaning purpose :

 sns.heatmap(df.isnull())
 sns.heatmap(df.isna())

 This quickly shows where missing values occur in your dataset.
"""

data2 = {
    "Raja":[90,80,70,100],
    "Rupak":[80,30,40,95],
    "Ayush":[50,85,25,None]
}
df2 = pd.DataFrame(data2)
sns.heatmap(df2.isnull())
plt.show()
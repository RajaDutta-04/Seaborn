import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data={
    "Name":['Raja','Rupak','Arnesh','Ayush'],
    "type":["Studious","NonStudious","Studious","NonStudious"],
    "cgpa":[9.14,8.88,8.13,7.5],
    "salary":[50000,75000,60000,90000]
}
df = pd.DataFrame(data)

sns.lineplot(x="cgpa",y="salary",data=df)
plt.show()

#Separate lines with category
sns.lineplot(x="cgpa",y="salary",data=df,hue="type")
plt.show()

#Line Style
sns.lineplot(x="cgpa",y="salary",data=df,hue="type",linestyle="--")
plt.show()

#Pallete parametre

""" A palette is simply a collection of colors.

     Instead of selecting one color, Seaborn selects different colors from the palette."""


"""
When Can We Use palette?

==> Only when Seaborn needs multiple colors, typically with parameters like:

    hue (and in some plot types, style combinations or multiple semantic mappings)
"""

sns.lineplot(x="cgpa",y="salary",data=df,hue="type",linestyle="--",palette="viridis")
plt.show()


"""
Most Used Palette

1. deep - default
2. Set2 - Presentations , College projects , Portfolio projects
3. Set1 - You want categories to stand out clearly , There are only a few categories.
4. tab10 - Up to 10 categories , Professional visualizations
5. colorblind - Sharing plots publicly , Creating accessible visualizations
6. viridis - Heatmaps , Continuous numeric values , Scientific visualizations
7. magma - Research papers , Scientific plots
8. rocket - Modern-looking and good for sequential data.
9. crest - Environmental data , Water/climate-related visualizations
10. flare - Continuous variables , Heatmaps

"""
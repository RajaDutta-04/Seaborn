"""
Violin Plot is used to measure how data is spreaded or the distribution of data

But it is different from histogram. Histogram can't compare category , but violinplot can.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "Student": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Gender": ["Male", "Male", "Female", "Female",
               "Male", "Female", "Male", "Female"],
    "Marks": [70, 85, 90, 78, 65, 88, 95, 72]
}

df = pd.DataFrame(data)

# sns.violinplot(x="Gender",y="Marks",data = df)
# plt.show()


"""
Parametres:
1. hue , palette
2. inner :  "box" → Small box plot inside
            "quart" → Quartile lines
            "point" → Individual points
            "stick" → Small sticks
            None → Nothing

3. split :  True or False
            Works only when using hue with exactly two levels.Instead of two violins we get two splitted violins.

4. cut :    Controls how far the violin extends beyond the data.
            cut=0 → Ends exactly at the minimum and maximum values.
            Larger values extend the density beyond the observed range.

5. orient : "h" ==> horizontal / "v" ==> vertical
"""

sns.violinplot(
    x="Gender",
    y="Marks",
    data = df,
    hue="Gender",
    inner="quart",
    split=True,
    cut = 0,
    orient="v"

)
plt.show()
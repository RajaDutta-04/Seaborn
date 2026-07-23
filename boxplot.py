import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Student": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Gender": ["Male", "Male", "Female", "Female",
               "Male", "Female", "Male", "Female"],
    "Marks": [70, 85, 90, 78, 65, 88, 95, 72]
}

df = pd.DataFrame(data)

sns.boxplot(x="Gender",y="Marks",data=df)
plt.show()

"""
What does a box plot show ?

    1. Minimum value (excluding outliers)
    2. First Quartile (Q1) - Median of the values that are lower than Q2.
    3. Median (Q2) - Median of the total values.
    4. Third Quartile (Q3) - Median of the values that are upper than Q2.
    5. Maximum value (excluding outliers)
    6. Whiskers - lines that connect the maximum and minimum values with the quartiles.

------------------------------------------------------------------------------------------
What is IQR?

    The Interquartile Range (IQR) measures the spread of the middle 50% of the data.
    Formula: IQR= Q3 - Q1

------------------------------------------------------------------------------------------

How are Outliers detected?

    An outlier is a value outside these limits:
    Lower limit: Q1 - 1.5 * IQR
    Upper limit: Q3 + 1.5 * IQR
"""

"""
Parametres:

showfliers - True (show outliers) / False (hide outliers)
"""

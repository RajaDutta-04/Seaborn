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
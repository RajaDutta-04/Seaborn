import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "marks": [50,40,20,10,40,60,30.50,65,85,35,65,15]
}

df = pd.DataFrame(data)

# sns.histplot(x="marks",bins=10,data=df)
# plt.show()



"""
For smooth density graph:

kde = True
"""
sns.histplot(x="marks",bins=10,data=df,kde=True)
plt.show()

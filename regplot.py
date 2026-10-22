import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Study Hours" : [4,5,6,7,9,10,15],
    "Exam Score" : [40,50,60,70,90,95,100]
}

df = pd.DataFrame(data)

sns.regplot(x="Study Hours",y="Exam Score",data=df)
plt.show()

#Use regplot when you want to see the relationship between two numeric variables and summarize its trend with a regression line.
#For example, plotting study hours against exam scores can show whether scores tend to rise as study time increases. The confidence band gives a sense of uncertainty around the estimated trend.
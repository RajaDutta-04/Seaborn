import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name":['Raja','Rahul','Subhankar','Jishu','Rupak','Arnesh','Ayush'],
    "StudyHour":[4,5,7,4,8,3,2],
    "Marks":[50,39,69,90,100,20,45]
}

df = pd.DataFrame(data)

# sns.scatterplot(x="StudyHour",y="Marks",palette="dark",data=df)
# plt.xlabel("Study Hours")
# plt.ylabel("Marks")
# plt.show()

"""
Parametres same as before

size - Point Size
"""
sns.scatterplot(x="StudyHour",y="Marks",palette="dark",data=df,size="Marks") #More Marks ==> Bigger point
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("fast")

data=pd.read_csv("line.csv")

age=data["Age"]
all_devs=data["All_Devs"]
python=data["Python"]

plt.plot(age,all_devs,label="All Developers")
plt.plot(age,python,label="Python")

plt.fill_between(age,python,all_devs,
                 where=(python>all_devs),interpolate=True,label="Above Average",alpha=0.25)

plt.fill_between(age,python,all_devs,
                 where=(python<=all_devs),interpolate=True,label="Below Average",alpha=0.25,color="red")


plt.legend()
plt.tight_layout()
plt.show()

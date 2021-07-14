import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("fast")

data = pd.read_csv("subplot.csv")
age = data["Age"]
python = data["Python"]
js = data["JavaScript"]
all_devs = data["All_Devs"]

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(age, python, label="Python")
ax1.plot(age, js, label="JavaScript")
ax1.set_ylabel("Median Salary (USD)")
ax1.set_title("Median Salary by age")
ax1.legend()

ax2.plot(age, all_devs, label="All Developers")
ax2.set_xlabel("Age")
ax2.set_ylabel("Median Salary (USD)")
ax2.legend()

plt.tight_layout()
plt.show()

fig.savefig("subplot.png")

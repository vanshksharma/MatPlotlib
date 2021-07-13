import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("fast")

data = pd.read_csv("Hist_Data.csv")
ages = data["Age"]
ids = data["Responder_id"]
median = 29

bins = np.arange(10, 101, 10)

plt.hist(ages, bins=bins, log=True, edgecolor="black")

plt.axvline(median, linewidth=2, color="red", label="Age Median")

plt.title("Age of Respondents")
plt.xlabel("Ages")
plt.ylabel("Total Respondents")

plt.legend()
plt.tight_layout()
plt.show()

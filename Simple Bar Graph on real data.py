import csv
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
plt.style.use("fivethirtyeight")

data=pd.read_csv("data.csv")

lang_responses=data["LanguagesWorkedWith"]

lang_counter=Counter()
for lang in lang_responses:
    lang_counter.update(lang.split(";"))

language,users=map(list,zip(*lang_counter.most_common(15)))

language.reverse()
users.reverse()

plt.barh(language,users,height=0.4,color="cornflowerblue")

plt.title("Most Popular Languages")

plt.xlabel("No. of people who use")
plt.tight_layout()

plt.show()


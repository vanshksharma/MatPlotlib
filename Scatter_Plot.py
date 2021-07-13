import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("fast")

data = pd.read_csv("Scatter_Data.csv")
views = data["view_count"]
likes = data["likes"]
ratio = data["ratio"]

plt.scatter(likes, views, c=ratio,cmap="summer")
cbar = plt.colorbar()
cbar.set_label("Like/Dislike Ratio")

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Likes")
plt.ylabel("Views")


plt.show()

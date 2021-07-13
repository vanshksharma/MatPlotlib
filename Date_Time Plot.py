import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates

plt.style.use("fast")

data = pd.read_csv("date-time.csv")

data["Date"] = pd.to_datetime(data["Date"])
data.sort_values("Date", inplace=True)

dates = data["Date"]
values = data["Close"]

plt.plot_date(dates, values, linestyle="solid")
plt.gcf().autofmt_xdate()

date_format=mpl_dates.DateFormatter("%b,%d %Y")
plt.gca().xaxis.set_major_formatter(date_format)

plt.xlabel("Dates")
plt.ylabel("Closing Value")
plt.title("Bitcoin Prices")
plt.tight_layout()
plt.show()

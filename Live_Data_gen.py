import csv
import time
import random

x_value = 0
total_1 = 1000
total_2 = 1000

fieldnames = ["x_value", "total_1", "total_2"]

csv_file = open("live.csv", 'w')
csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
csv_writer.writeheader()

while True:
    csv_file = open("live.csv", "a")
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    info = {"x_value": x_value, "total_1": total_1, "total_2": total_2}
    csv_writer.writerow(info)

    print(x_value, total_1, total_2)

    x_value += 1
    total_1 += random.randint(-10, 10)
    total_2 += random.randint(-6, 8)
    time.sleep(0.5)

import matplotlib.pyplot as plt

plt.style.use("fast")
language=['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
users=[59219, 55466, 47544, 36443, 35917]
explode=[0,0,0,0.1,0]
plt.pie(users,labels=language,explode=explode,startangle=90,autopct="%1.1f%%")

plt.show()

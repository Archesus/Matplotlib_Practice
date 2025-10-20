import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.array([2020, 2021, 2022, 2023, 2024])  # using np array as its faster than native python lists
y1 = np.array([15, 20, 25, 17, 30])
y2 = np.array([17, 28, 32, 5, 42])

# # setting the title of the plot and customize its appearance
plt.title("Class Size",   
        fontsize=20, 
        family="Arial",
        fontweight="bold"
)

# # setting the label of the x and y axis
plt.xlabel("Year", 
            fontweight="medium",
            color="#010340" 
            )
plt.ylabel("No. of students", 
           fontweight="medium",
           color="#010340"
           )

# # plotting the lists and customizing its appearance
plt.plot(x, y1, 
         marker=".", 
         markersize=20, 
         markerfacecolor="#9803fc", 
         markeredgecolor="#9803fc", 
         linestyle="dashed", 
         linewidth=2, 
         color="#6b03fc"
)

plt.plot(x, y2,
         marker=".", 
         markersize=20, 
         markerfacecolor="#03fca1", 
         markeredgecolor="#03fca1", 
         linestyle="dashed", 
         linewidth=2, 
         color="#0bfc03"
)

plt.tick_params(axis="both",
                colors="#010340"
                )

# only uses the values mentioned in the list as the x-axis
plt.xticks(x)

# making grids to improve readability
plt.grid(True, color="lightgray")

plt.show()


# Bar charts
categories = ["Grains", "Fruit", "Vegetables", "Protein", "Dairy"]
values = np.array([4, 5, 3, 2, 5])

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.bar(categories, values, color="#893de0")
plt.show()

# Pie Charts

categories = ["Freshmen", "Sophomore", "Juniors", "Seniors"]
values = np.array([155, 132, 224, 75])

plt.title("Different student categories")

plt.pie(values, labels=categories, autopct="%1.1f%%", explode=[0, 0, 0, 0.2], shadow=True, startangle=90)
plt.show()


# Scatter Plot
x = np.array([1, 2, 2, 1, 3, 4, 5, 6])
y = np.array([55, 65, 58, 50, 80, 92, 95, 98])

x2 = np.array([1, 3, 2, 1, 5, 6, 6, 7])
y2 = np.array([42, 68, 51, 40, 80, 82, 92, 94])

plt.scatter(x, y, s= 150, alpha=0.75, label="Class A")   # alpha is used for opacity and label is used to label the dots
plt.scatter(x2, y2, s= 150, alpha=0.75, color="red", label="Class B")
plt.legend()  # to show the labels as lengend
plt.show()

# # Histogram

scores = np.random.normal(loc=80, scale=10, size=100)
plt.hist(scores, bins=10, color="lightgreen", edgecolor="black")

plt.title("Student scores")

plt.show()


# Subplots

x = np.array([1, 2, 3, 4, 5])

figure, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, x*2, color="blue")
axes[0, 0].set_title("x*2")

axes[0, 1].plot(x, x**2, color="red")
axes[0, 1].set_title("x**2")

axes[1, 0].plot(x, x**3, color="green")
axes[1, 0].set_title("x**3")

axes[1, 1].plot(x, x**4, color="purple")
axes[1, 1].set_title("x**4")

plt.tight_layout()
plt.show()


# using matplotlib with pandas
df = pd.read_csv("data.csv")
type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color="#e0c83d", edgecolor="black")
plt.title("Number of Pokemon by primary types")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()
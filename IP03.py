import matplotlib.pyplot as plt

#PREDEFINED DATA
grades= { 
    "stu1": 87,
    "stu2": 56,
    "stu3": 90,
    "stu4": 94,
    "stu5": 75
    }
#PIE-CHART
plt.figure(figsize(10,5))
plt.subplot(1, 2, 1)
plt.pie(grades.values(), labels=grades.keys(), autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Student Grades")

#BAR GRAPH
plt.subplot(1, 2, 2)
plt.bar(grades.keys(), grades.values(), color=["green", "blue", "orange", "red", "purple"])
plt.title("Number of Students per Grade")
plt.xlabel("Grades")
plt.ylabel("Number of Students")

plt.tight_layout()
#DISPLAY
plt.show()
print("DONE")
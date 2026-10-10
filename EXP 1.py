import numpy as np


student_scores = np.array([
    [85, 90, 78, 88],
    [92, 86, 89, 80],
    [76, 95, 84, 90],
    [88, 82, 91, 85]
])

subjects = ["Math", "Science", "English", "History"]

averages = np.mean(student_scores, axis=0)

for i in range(len(subjects)):
    print(subjects[i], "Average:", averages[i])

highest_index = np.argmax(averages)

print("Highest average subject:", subjects[highest_index])
print("Highest average score:", averages[highest_index])

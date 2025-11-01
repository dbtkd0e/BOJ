score = int(input())

grade = ['A','B','C','D','F']
idx = 0
if score < 60:
    idx = 4
elif score < 70:
    idx = 3
elif score < 80:
    idx = 2
elif score < 90:
    idx = 1

print(grade[idx])
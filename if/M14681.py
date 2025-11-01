x = int(input())
y = int(input())
result = 1
if x > 0:
    if y < 0:
        result = 4
else:
    if y < 0:
        result = 3
    else:
        result = 2
print(result)
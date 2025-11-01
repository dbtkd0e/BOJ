a1,b1,c1 = map(int, input())
a2,b2,c2 = map(int, input())

results = []
results.append(c2*(c1+b1*10+a1*100))
results.append((b2*(c1+b1*10+a1*100))*10)
results.append((a2*(c1+b1*10+a1*100))*100)

result = 0
for idx,ele in enumerate(results):
    result += ele
    if idx > 0:
        ele /= 10**idx
    print(int(ele))
    
print(result)

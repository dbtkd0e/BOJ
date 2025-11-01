A, B = map(int, input().split(" "))

ans = [">","<","=="]
point = 0

if A<B:
    point = 1
elif A==B:
    point = 2

print(ans[point])

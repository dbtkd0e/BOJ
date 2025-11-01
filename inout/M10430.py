A, B, C = map(int, input().split(" "))
output1 = (A+B)%C
output2 = ((A%C) + (B%C))%C
output3 = (A*B)%C
output4 = ((A%C) * (B%C))%C

list_out = [output1, output2, output3, output4]

for element in list_out:
    print(element)
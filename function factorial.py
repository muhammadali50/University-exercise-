def fct (num):
    return num 
x = fct(5)
y = 1
for i in range(1,x):
    y = y * i
    x -=1
print(y)
import random
import time
#додаткове завдання: генерувати а в діапазоні (1..50),вивести час виконання програми
start = time.time()
a0 = (random.randint(1,50))
a1 = (random.randint(1,50))
a2 = (random.randint(1,50))
a3 = (random.randint(1,50))
X1 = [random.randrange(1,21,1) for i in range(8)]
X2 = [random.randrange(1,21,1) for i in range(8)]
X3 = [random.randrange(1,21,1) for i in range(8)]
Y = [a0 + a1*X1[i] + a2*X2[i] + a3*X3[i] for i in range(8)]
X01 = (max(X1)+min(X1))/2
X02 = (max(X2)+min(X2))/2
X03 = (max(X3)+min(X3))/2
dX1 = X01-min(X1)
dX2 = X02-min(X2)
dX3 = X03-min(X3)
Xn1 = [(X1[i] - X01)/dX1 for i in range(8)]
Xn2 = [(X2[i] - X02)/dX2 for i in range(8)]
Xn3 = [(X3[i] - X03)/dX3 for i in range(8)]
Yet = a0 + a1*X01 + a2*X02 + a3*X03
f = [(Y[i]-Yet)**2 for i in range(8)]
res = max(f)
print("a0=%s a1=%s a2=%s a3=%s"%(a0, a1, a2, a3))
print("X1: %s"%X1)
print("X2: %s"%X2)
print("X3: %s"%X3)
print("Y: %s"%Y)
print("x0: %s %s %s"%(X01, X02, X03))
print("dx: %s %s %s"%(dX1, dX2, dX3))
print("Xн1: %s"%Xn1)
print("Xн2: %s"%Xn2)
print("Xн3: %s"%Xn3)
print("Yэт: %s"%Yet)
print("(Y-Yэт)²: %s"%f)
print("max(Y-Yэт)²: %s"%res)
print("Час роботи програми в секундах:", time.time() - start)



set1 = set()
set2 = set()

for i in range(1,10):
    set1.add(i)
for i in range(9,0,-1):    
    set2.add(i)


print(set1)
print(set2)

if set1 == set2:
    print("Sets iguales")
else:
    print("sets diferentes")
for i in range (5) :
    print("*" * 7)


for i in range (5) :
    for j in range (5) :
        if i == 2 or i == 2:
            print("*", end=" ")
        elif j == 2 or j ==2:
            print("*", end=" ")
        else:
            print("-", end=" ")    
    print()       
        

# n = 5 n-1
for x in range (5) :
    for y in range (5) :
        if x == 0 or x == 5-1 or y == 0 or y == 5-1:
            print("*", end=" ")
        else:
            print("-", end=" ")    
    print()               




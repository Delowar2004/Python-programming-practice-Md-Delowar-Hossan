# Python Pattern Designe 33 N Alphabet Shape Star Pattern Python Program
x = input("Enter Pattern Print View value: ")

for row in range(0,7):
    for col in range(0,7):
        if(col==0 or col==6 or row==col and (col>0 and col<6)):
            print(x," ",end="")
        else:
            print("   ",end="")
    print()
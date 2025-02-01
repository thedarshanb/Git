pin ="5416"
trail =1
while trail <=3:
    inpin=input(f"Trail-{trail} |pin>>")
    trail +=1
    if inpin ==pin:
        print("correct")
        break
    else:
        print("Incorrect")

pin ="123"
while True:
    inp=input("Enter the pin>>")
    if pin ==inp:
        print("correct")
        break
    else:
        print("incorrect")

i=1
while True:
    print("try",i)
    i=i+1
    if i>100:
        i=i+1
        break
print("give up")

i=0
while i<10:
    i +=1
    if i==7:
        print("skip:",i)
        continue
    print(i)

for i in range(1,6):
    for j in range(1,6):
        print(f"{i}x{j}={i*j}")
        
    print("")


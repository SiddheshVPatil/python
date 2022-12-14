# for loops
name="Siddhesh"
for i in name:
    print(i)
    if(i=="e"):
        print("WOW!!!")
        
print("---------------------")   
 
colors=["red","blue","green","yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)
        
print("---------------------")

for k in range(5):
    print(k)
    
print("---------------------")
for k in range(1,8):
    print(k)
    
print("---------------------")
for k in range(1,20,2):# start from 1; stops at 20-1;gap of 2.
    print(k)
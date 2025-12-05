# the dial is 50 left
dial=50
count=0
direction='L'
file= open("day1_input.txt","r")

for line in file:
    line=line.strip()
    dir=line[0]
    move=int(line[1:len(line)])

    
    if dir=='L':
        dial = (dial - move)%100
    elif dir=='R':
        dial = (dial + move)%100 
    
    # checking if the dial is 0
    if dial==0:
        count+=1
print(count)
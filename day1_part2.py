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
        for i in range(move):
            dial-=1
            if dial%100==0:
                count+=1

    elif dir=='R':
        for i in range(move):
            dial+=1
            if dial%100==0:
                count+=1
    dial=dial%100
    # # checking if the dial is 0
    # if dial==0:
    #     count+=1
print(count)                    
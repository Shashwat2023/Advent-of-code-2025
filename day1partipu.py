dial = 50

count = 0 

def crosses_boundary(old , new):
    return old //100 != new //100
with open("day1_input_part1.txt" , "r") as f:
    for line in f:
        line= line.strip()

        if not line:
            continue
    
    dir  = line[0]

    value = int(line[1:])

    old = dial 
    if dir =="R":
        dial += value
    elif dir == 'L':
        dial -= value
    
    if crosses_boundary(old , dial):
        count += 1
    
print(count)

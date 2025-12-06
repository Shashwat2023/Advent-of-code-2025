fname="day2_input.txt"
count= 0

with open(fname,'r') as f:
    for line in f:
        ranges = line.strip().split(",")
        for r in ranges:
            start_range, end_range = r.split("-")
            start_range=int(start_range)
            end_range = int(end_range)



            for i in range(start_range, end_range + 1): 
                s = str(i)
                if len(s) % 2 == 0:  
                    mid = len(s) // 2
                    if s[:mid] == s[mid:]:  
                        count += i

print(count)

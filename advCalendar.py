def countIncrease_day1():
    total = 0 
    prev = -1
    lines = []
    with open('inputs/day1.txt') as f:
        lines = f.read().splitlines()

    for curr in lines:
        curr = int(curr)
        if prev != -1:
            if curr >= prev:
                total += 1
        prev = curr

    return total

def dive_day2():
    horizontal = 0
    depth = 0 
    lines = []
    with open('inputs/day2.txt') as f:
        lines = f.read().splitlines()
    
    for i in lines:
        move, amount = i.split(' ',1)
        amount = int(amount)
        if 'down' == move:
            depth += amount
        elif 'forward' == move:
            horizontal += amount
        elif 'up' == move:
            depth -= amount
        
    total = depth * horizontal
    return total 

if __name__ == "__main__":
    print("Day 1: " + str(countIncrease_day1()))
    print("Day 2: " + str(dive_day2()))


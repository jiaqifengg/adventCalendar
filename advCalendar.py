def countIncrease_day1():
    total = 0 
    prev = -1
    lines = []
    with open('day1.txt') as f:
        lines = f.read().splitlines()

    for curr in lines:
        curr = int(curr)
        if prev != -1:
            if curr >= prev:
                total += 1
                prev = curr
        prev = curr
    print(total)

if __name__ == "__main__":
    countIncrease_day1()

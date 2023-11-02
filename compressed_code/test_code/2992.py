def solution():
    
    base = 1
    total = 0
    for i in range(4):
        level = base * base
        total += level
        base += 1

    result = total
    return result

print(solution())
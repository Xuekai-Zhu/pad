def solution():
    temps = [-36, 13, -15, -10]
    total = 0
    for temp in temps:
        total = total + temp
    avg = total / len(temps)
    result = avg
    return result

print(solution())
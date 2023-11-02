def solution():
    temperatures = [40, 50, 65, 36, 82, 72, 26]
    sum = 0
    for temp in temperatures:
        sum += temp
    average = sum / len(temperatures)
    result = average
    return result

print(solution())
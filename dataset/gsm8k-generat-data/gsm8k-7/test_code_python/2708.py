def solution():
    months = ['January', 'February', 'March', 'April', 'May']
    current_savings = 10

    for month in range(1, 5):
        current_savings *= 2

    result = current_savings
    return result

print(solution())
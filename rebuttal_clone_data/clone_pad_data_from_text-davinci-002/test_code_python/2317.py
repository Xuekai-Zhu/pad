def solution():
    items = [25.50, 35.00, 13.50, 13.50, 8.50, 6.00, 6.00]
    total = sum(items)
    tip = total * 0.20
    result = total + tip
    return result

print(solution())
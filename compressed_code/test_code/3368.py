def solution():
    
    liam_oranges = 40
    claire_oranges = 30
    liam_price = 2.5
    claire_price = 1.2
    liam_total = (liam_oranges // 2) * liam_price + (liam_oranges % 2) * (liam_price / 2)
    claire_total = claire_oranges * claire_price
    total = liam_total + claire_total
    result = total
    return result

print(solution())
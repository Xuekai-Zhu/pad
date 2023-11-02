def solution():
    """Liam and Claire picked and sold oranges to save for their mother's birthday gift. Liam picked 40 oranges and sold them at $2.50 for 2 while Claire picked 30 oranges and sold them at $1.20 each. If all of their oranges were sold, how much are they going to save for their mother's birthday gift?"""
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
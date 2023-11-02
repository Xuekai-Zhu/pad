def solution():
    """Martha is knitting winter wear for her 3 grandchildren. They're triplets, so they're all the same size. She wants to make a hat, scarf, sweater, mittens, and socks for each of them. It takes 2 skeins of wool to make a hat, 4 for a scarf, 12 for a sweater, 1 for a pair of mittens, and 2 for a pair of socks. How many skeins of wool will she need to buy?"""
    hats = 3 * 2
    scarfs = 3 * 4
    sweaters = 3 * 12
    mittens = 3 * 1
    socks = 3 * 2
    total_skeins = hats + scarfs + sweaters + mittens + socks
    result = total_skeins
    return result

print(solution())
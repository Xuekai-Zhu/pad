def solution():
    # Let's call the number of toys Mandy has "m"
    m = None 

    # Anna has 3 times as many toys as Mandy
    a = 3 * m 

    # Amanda has 2 more toys than Anna
    am = a + 2 

    # Together, they have 142 toys
    total_toys = m + a + am 

    # We can use algebra to solve for m:
    # m + 3m + (3m + 2) = 142
    # 7m + 2 = 142
    # 7m = 140
    # m = 20

    m = 20
    result = m
    return result

print(solution())
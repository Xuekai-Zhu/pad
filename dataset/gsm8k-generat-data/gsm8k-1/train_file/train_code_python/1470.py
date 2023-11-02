def solution():
    """Karen's class fund contains only $10 and $20 bills, which amount to $120. The number of $10 bills is twice as many $20 bills. How many $20 bills do they have in their fund?"""
    total_money = 120
    x = 2
    y = 1
    while x * 10 + y * 20 != total_money:
        if x * 10 + y * 20 > total_money:
            y -= 1
            x += 2
        else:
            y += 1
    result = y
    return result

print(solution())
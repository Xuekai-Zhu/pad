def solution():
    """Tamara, Nora, and Lulu have been saving to pay off a $40 debt. So far, Nora has saved five times what Lulu has, but three times Tamara’s savings. Lulu has saved $6. If they pay off the debt and divide the remaining money equally, how many dollars will each girl get?"""
    total_savings = 6 + (5 * 6) + ((1/3) * (5 * 6))
    remaining_money = total_savings - 40
    each_girl_gets = remaining_money / 3
    result = each_girl_gets
    return result

print(solution())
def solution():
    """Francie saves up her allowance for several weeks. She receives an allowance of $5 a week for 8 weeks. Then her dad raises her allowance, and she receives $6 a week for 6 weeks. Francie uses half of the money to buy new clothes. With the remaining money, she buys a video game that costs $35. How much money does Francie have remaining after buying the video game?"""
    weeks1 = 8
    allowance1 = 5
    weeks2 = 6
    allowance2 = 6
    total_allowance = weeks1 * allowance1 + weeks2 * allowance2
    clothes_cost = total_allowance / 2
    remaining_money = total_allowance - clothes_cost - 35
    result = remaining_money
    return result

print(solution())
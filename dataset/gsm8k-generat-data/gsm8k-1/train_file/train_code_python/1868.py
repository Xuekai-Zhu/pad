def solution():
    """Francie saves up her allowance for several weeks. She receives an allowance of $5 a week for 8 weeks. Then her dad raises her allowance, and she receives $6 a week for 6 weeks. Francie uses half of the money to buy new clothes. With the remaining money, she buys a video game that costs $35. How much money does Francie have remaining after buying the video game?"""
    weeks_before_raise = 8
    allowance_before_raise = 5
    weeks_after_raise = 6
    allowance_after_raise = 6
    clothes_cost = (weeks_before_raise * allowance_before_raise + weeks_after_raise * allowance_after_raise) / 2
    remaining_money = (weeks_before_raise * allowance_before_raise + weeks_after_raise * allowance_after_raise - clothes_cost) - 35
    result = remaining_money
    return result

print(solution())
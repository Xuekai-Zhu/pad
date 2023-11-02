def solution():
    """Francie saves up her allowance for several weeks. She receives an allowance of $5 a week for 8 weeks. Then her dad raises her allowance, and she receives $6 a week for 6 weeks. Francie uses half of the money to buy new clothes. With the remaining money, she buys a video game that costs $35. How much money does Francie have remaining after buying the video game?"""
    # Calculate the total allowance from the first 8 weeks
    allowance1 = 5 * 8

    # Calculate the total allowance from the next 6 weeks with the increased amount
    allowance2 = 6 * 6

    # Calculate the total amount of money saved up
    total_money = allowance1 + allowance2

    # Calculate the amount spent on new clothes
    clothes_cost = total_money / 2

    # Calculate the remaining amount after buying the video game
    remaining_money = total_money - clothes_cost - 35

    result = remaining_money
    return result

print(solution())
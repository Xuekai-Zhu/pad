def solution():
    """Francie saves up her allowance for several weeks. She receives an allowance of $5 a week for 8 weeks. Then her dad raises her allowance, and she receives $6 a week for 6 weeks. Francie uses half of the money to buy new clothes. With the remaining money, she buys a video game that costs $35. How much money does Francie have remaining after buying the video game?"""
    # Define the allowance amount for the first 8 weeks
    ALLOWANCE_1 = 5
    WEEKS_1 = 8

    # Define the allowance amount for the next 6 weeks
    ALLOWANCE_2 = 6
    WEEKS_2 = 6

    # Calculate the total amount of money Francie received
    total_money = (ALLOWANCE_1 * WEEKS_1) + (ALLOWANCE_2 * WEEKS_2)

    # Calculate the amount of money Francie spent on clothes
    clothes_money = total_money / 2

    # Calculate the amount of money Francie had left after buying the video game
    remaining_money = total_money - clothes_money - 35

    # Display the remaining amount of money
    result = remaining_money
    return result

print(solution())
def solution():
    """Bill the miner discovers a vein of fool's gold. He successfully sells 8 ounces to a merchant, but when he tries to sell to the sheriff he's arrested, fined $50 and run out of town on a rail. If Bill earned $9 for every ounce of fool's gold he sold, how much money is he left with?"""
    # Define the amount of fool's gold sold and the price per ounce
    ounces_sold = 8
    price_per_ounce = 9

    # Calculate the total earnings and the fine
    total_earnings = ounces_sold * price_per_ounce
    fine = 50

    # Calculate the money left after paying the fine
    money_left = total_earnings - fine

    # Return the result
    result = money_left
    return result

print(solution())
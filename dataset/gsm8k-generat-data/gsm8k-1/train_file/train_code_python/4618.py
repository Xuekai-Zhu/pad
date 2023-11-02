def solution():
    """Bill the miner discovers a vein of fool's gold. He successfully sells 8 ounces to a merchant, but when he tries to sell to the sheriff he's arrested, fined $50 and run out of town on a rail. If Bill earned $9 for every ounce of fool's gold he sold, how much money is he left with?"""
    ounces_sold = 8
    price_per_ounce = 9
    earnings = ounces_sold * price_per_ounce
    fine = 50
    left_with = earnings - fine
    result = left_with
    return result

print(solution())
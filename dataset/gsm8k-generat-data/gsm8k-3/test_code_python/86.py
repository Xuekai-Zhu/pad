def solution():
    """Peter goes to the store to buy a soda. The soda costs $.25 an ounce. He brought $2 with him and leaves with $.50. How many ounces of soda did he buy?"""
    # Define the price per ounce of soda
    price_per_ounce = 0.25

    # Define the amount of money Peter brought with him and the amount of money he spent
    initial_money = 2.0
    final_money = 2.5

    # Calculate the amount of money spent on soda
    soda_money = initial_money - final_money

    # Calculate the number of ounces of soda bought
    soda_ounces = soda_money / price_per_ounce

    # return the result
    result = soda_ounces
    return result

print(solution())
def solution():
    """Peter goes to the store to buy a soda. The soda costs $.25 an ounce. He brought $2 with him and leaves with $.50. How many ounces of soda did he buy?"""
    
    # Define the initial amount of money Peter brought with him
    initial_money = 2

    # Define the amount of money Peter had left after buying the soda
    left_money = 0.5

    # Define the cost of 1 ounce of soda 
    price_per_ounce = 0.25

    # Calculate the total amount of money Peter spent on the soda 
    spent_money = initial_money - left_money 

    # Calculate the total amount of soda bought
    total_ounces = spent_money / price_per_ounce

    result = total_ounces
    return result

print(solution())
def solution():
    """John decides to buy a month's supply of dog treats. He gives his dog 2 treats a day and they cost $.1 each. How much does he spend on the treats if the month is 30 days long?"""
    # Define the number of dog treats he gives his dog per day and the price per treat
    treats_per_day = 2
    price_per_treat = 0.1

    # Calculate the total number of dog treats for the month
    total_treats = treats_per_day * 30

    # Calculate the total cost of the dog treats for the month
    total_cost = total_treats * price_per_treat

    # Return the result
    result = total_cost
    return result

print(solution())
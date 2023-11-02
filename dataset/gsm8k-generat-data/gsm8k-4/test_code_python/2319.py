def solution():
    """Mr. Mayer bought Corgi dogs for $1000 each. He plans to sell them with a 30% profit. If one of his friends wants to buy two dogs, how much should his friend pay?"""
    # Define the cost and profit percentage
    cost = 1000
    profit_percentage = 30

    # Calculate the profit on each dog
    profit_per_dog = cost * (profit_percentage / 100)

    # Calculate the selling price of each dog
    selling_price = cost + profit_per_dog

    # Calculate the total cost for 2 dogs
    total_cost = selling_price * 2

    # Return the result
    result = total_cost
    return result

print(solution())
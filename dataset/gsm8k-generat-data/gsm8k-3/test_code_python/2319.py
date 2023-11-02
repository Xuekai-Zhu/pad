def solution():
    """Mr. Mayer bought Corgi dogs for $1000 each. He plans to sell them with a 30% profit. If one of his friends wants to buy two dogs, how much should his friend pay?"""
    # Define the cost of one Corgi dog and the desired profit percentage
    dog_cost = 1000
    profit_percentage = 0.3

    # Calculate the selling price of one dog with the desired profit
    selling_price = dog_cost + (dog_cost * profit_percentage)

    # Calculate the total cost for two dogs
    total_cost = 2 * selling_price

    # Display the cost for two dogs
    result = total_cost
    return result

print(solution())
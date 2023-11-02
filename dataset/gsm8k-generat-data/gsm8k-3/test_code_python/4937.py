def solution():
    """The difference between the price of an orange and the price of a pear equals the price of a banana. If the total cost of an orange and a pear is $120 and a pear costs $90, calculate the total price of buying 200 bananas and twice as many oranges as bananas."""
    # Define the cost of a pear
    pear_cost = 90

    # Calculate the cost of an orange
    orange_cost = 120 - pear_cost

    # Calculate the cost of a banana
    banana_cost = orange_cost

    # Calculate the total cost of buying 200 bananas
    total_banana_cost = 200 * banana_cost

    # Calculate the number of oranges to buy
    num_oranges = 2 * 200

    # Calculate the total cost of buying the oranges
    total_orange_cost = num_oranges * orange_cost

    # Calculate the total cost of buying all the fruit
    total_cost = total_banana_cost + total_orange_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())
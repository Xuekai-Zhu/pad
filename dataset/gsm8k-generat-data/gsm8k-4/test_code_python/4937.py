def solution():
    """The difference between the price of an orange and the price of a pear equals the price of a banana. If the total cost of an orange and a pear is $120 and a pear costs $90, calculate the total price of buying 200 bananas and twice as many oranges as bananas."""
    # Define the cost of a pear and the total cost of an orange and a pear
    pear_cost = 90
    orange_pear_total_cost = 120

    # Calculate the cost of an orange
    orange_cost = orange_pear_total_cost - pear_cost

    # Calculate the cost of a banana
    banana_cost = orange_cost

    # Calculate the total cost of buying 200 bananas
    total_banana_cost = banana_cost * 200

    # Calculate the number of oranges to buy
    num_oranges = 2 * 200

    # Calculate the total cost of buying the oranges
    total_orange_cost = num_oranges * orange_cost

    # Calculate the overall total cost
    overall_total_cost = total_banana_cost + total_orange_cost

    # return the result
    result = overall_total_cost
    return result

print(solution())
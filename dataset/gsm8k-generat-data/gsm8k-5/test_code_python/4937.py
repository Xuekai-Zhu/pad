def solution():
    # Calculate the price of an orange
    cost_orange = 120 - 90  # The cost of an orange and a pear is $120, and the pear costs $90
    # Calculate the price of a banana
    cost_banana = cost_orange

    # Calculate the total cost of 200 bananas
    total_banana_cost = cost_banana * 200

    # Calculate the number of oranges needed
    num_oranges = 2 * 200  # Twice as many oranges as bananas

    # Calculate the total cost of the oranges
    total_orange_cost = num_oranges * cost_orange

    # Calculate the total cost of buying 200 bananas and twice as many oranges as bananas
    total_cost = total_banana_cost + total_orange_cost
    result = total_cost
    return result

print(solution())
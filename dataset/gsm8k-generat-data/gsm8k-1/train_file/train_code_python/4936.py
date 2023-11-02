def solution():
    """The difference between the price of an orange and the price of a pear equals the price of a banana. If the total cost of an orange and a pear is $120 and a pear costs $90, calculate the total price of buying 200 bananas and twice as many oranges as bananas."""
    pear_cost = 90
    orange_cost = 120 - pear_cost
    banana_cost = orange_cost
    total_bananas = 200
    total_oranges = 2 * total_bananas
    total_orange_cost = total_oranges * orange_cost
    total_banana_cost = total_bananas * banana_cost
    total_cost = total_orange_cost + total_banana_cost
    result = total_cost
    return result

print(solution())
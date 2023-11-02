def solution():
    """The difference between the price of an orange and the price of a pear equals the price of a banana.
    If the total cost of an orange and a pear is $120 and a pear costs $90,
    calculate the total price of buying 200 bananas and twice as many oranges as bananas."""
    # Let's assume the price of a banana is x
    pear_price = 90
    orange_price = pear_price + x
    orange_quantity = 2 * 200
    total_orange_cost = orange_quantity * orange_price
    total_banana_cost = 200 * x
    total_cost = total_orange_cost + total_banana_cost + 120  # adding the cost of pear
    result = total_cost
    return result

print(solution())
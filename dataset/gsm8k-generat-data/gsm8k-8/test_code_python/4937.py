def solution():
    # Calculate the price of a banana
    banana_price = 120 - 90
    # Calculate the price of an orange
    orange_price = banana_price
    # Calculate the total cost of two oranges and one pear
    total_cost = 2 * orange_price + 90
    # Calculate the cost of one orange
    single_orange_price = (total_cost - 90) / 2
    # Calculate the cost of one banana
    single_banana_price = single_orange_price
    # Calculate the total cost of 200 bananas
    banana_total_cost = single_banana_price * 200
    # Calculate the total cost of twice as many oranges as bananas
    orange_total_cost = single_orange_price * 400
    # Calculate the total price of buying 200 bananas and twice as many oranges as bananas
    total_price = banana_total_cost + orange_total_cost
    result = total_price
    return result

print(solution())
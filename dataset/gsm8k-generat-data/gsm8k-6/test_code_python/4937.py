def solution():
    # Calculate the price of an orange
    price_pear = 90
    price_orange = 120 - price_pear  # the total cost of an orange and a pear is $120

    # Calculate the price of a banana
    price_banana = price_orange - price_pear  # the difference between the price of an orange and a pear equals the price of a banana

    # Calculate the total cost of buying 200 bananas
    cost_bananas = 200 * price_banana

    # Calculate the number of oranges (twice as many as bananas)
    num_oranges = 2 * 200

    # Calculate the total cost of buying oranges
    cost_oranges = num_oranges * price_orange

    # Calculate the total price
    total_price = cost_bananas + cost_oranges
    result = total_price
    return result

print(solution())
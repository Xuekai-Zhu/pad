def solution():
    # Calculate the price of the first 3 pieces of art
    price_first_3 = 45000 / 3

    # Calculate the price of the next piece of art
    price_next = price_first_3 * 1.5

    # Calculate the total cost of all the art
    total_cost = 4 * price_first_3 + price_next
    result = total_cost
    return result

print(solution())
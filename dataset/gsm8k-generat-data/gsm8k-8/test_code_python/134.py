def solution():
    # Calculate the price of two child tickets after the discount
    child_price = 109 - 5
    total_child_price = 2 * child_price

    # Calculate the price of two adult tickets
    adult_price = 109 * 2

    # Calculate the total price
    total_price = total_child_price + adult_price

    # Calculate the change
    change = 500 - total_price
    result = change
    return result

print(solution())
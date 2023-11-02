def solution():
    white_price = 5.0
    swiss_price = 6.0
    blue_price = 8.0
    package_size = 200  # grams

    # Calculate the amount of white cheese needed
    white_amount = 5 * package_size * (2/3)

    # Calculate the total cost of white cheese
    total_white_cost = white_amount / package_size * white_price

    # Calculate the total cost of swiss cheese
    total_swiss_cost = 5 * swiss_price

    # Calculate the total cost of blue cheese
    total_blue_cost = (600 / package_size) * blue_price

    # Calculate the total cost of all cheese
    total_cost = total_white_cost + total_swiss_cost + total_blue_cost
    result = total_cost
    return result

print(solution())
def solution():
    """The price of candy bars is twice the cost of caramel, and the cost of cotton candy is half the price of 4 candy bars. If the price of 1 caramel is $3, how much do 6 candy bars, 3 caramel, and 1 cotton candy cost together?"""
    # Define the cost of 1 caramel
    caramel_cost = 3

    # Calculate the price of 1 candy bar
    candybar_price = 2 * caramel_cost

    # Calculate the price of 4 candy bars
    four_candybars_price = 4 * candybar_price

    # Calculate the price of 1 cotton candy
    cotton_candy_price = 0.5 * four_candybars_price

    # Calculate the total cost of 6 candy bars
    six_candybars_cost = 6 * candybar_price

    # Calculate the total cost of 3 caramel
    three_caramel_cost = 3 * caramel_cost

    # Calculate the total cost of 1 cotton candy
    one_cottoncandy_cost = cotton_candy_price

    # Calculate the total cost of all items
    total_cost = six_candybars_cost + three_caramel_cost + one_cottoncandy_cost

    result = total_cost
    return result

print(solution())
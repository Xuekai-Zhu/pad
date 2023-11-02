def solution():
    initial_amount = 20
    peach_price = 2
    pounds_of_peaches = 3

    # Calculate the cost of the peaches
    peach_cost = peach_price * pounds_of_peaches

    # Calculate the amount Ines has left
    amount_left = initial_amount - peach_cost
    result = amount_left
    return result

print(solution())
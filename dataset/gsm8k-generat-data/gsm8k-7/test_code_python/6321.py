def solution():
    num_salads = 2
    salad_price = 3

    beef_weight = 2
    beef_price = 2 * salad_price

    potato_weight = 1
    potato_price = salad_price / 3

    juice_volume = 2
    juice_price = 1.5

    # Calculate the total cost of all salads
    total_salad_cost = num_salads * salad_price

    # Calculate the total cost of all beef
    total_beef_cost = beef_weight * beef_price

    # Calculate the total cost of all potatoes
    total_potato_cost = potato_weight * potato_price

    # Calculate the total cost of all juice
    total_juice_cost = juice_volume * juice_price

    # Calculate the total cost of all items
    total_cost = total_salad_cost + total_beef_cost + total_potato_cost + total_juice_cost
    result = total_cost
    return result

print(solution())
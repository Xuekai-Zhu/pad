def solution():
    # Define Randy's starting amount
    starting_amount = 30

    # Subtract the amount he spent on lunch
    remaining_amount = starting_amount - 10

    # Calculate the amount he spent on an ice cream cone
    ice_cream_cost = remaining_amount / 4

    # Subtract the amount he spent on the ice cream cone
    final_amount = remaining_amount - ice_cream_cost

    result = final_amount
    return result

print(solution())
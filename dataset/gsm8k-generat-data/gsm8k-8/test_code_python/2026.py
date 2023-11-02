def solution():
    # Define the initial amount Inez has
    initial_amount = 150

    # Calculate the amount spent on hockey skates
    skates_cost = initial_amount / 2

    # Calculate the remaining amount after buying hockey skates
    remaining_amount = initial_amount - skates_cost

    # Calculate the cost of hockey pads
    pads_cost = remaining_amount - 25

    result = pads_cost
    return result

print(solution())
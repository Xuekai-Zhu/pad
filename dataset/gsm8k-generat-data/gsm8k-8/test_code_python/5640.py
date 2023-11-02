def solution():
    # Calculate the total cost of the black ink
    black_ink_cost = 11 * 2

    # Calculate the total cost of the red ink
    red_ink_cost = 15 * 3

    # Calculate the total cost of the yellow ink
    yellow_ink_cost = 13 * 2

    # Calculate the total cost of all the printer inks
    total_ink_cost = black_ink_cost + red_ink_cost + yellow_ink_cost

    # Calculate how much more money Phantom needs to ask his mom
    additional_cost = total_ink_cost - 50
    result = additional_cost
    return result

print(solution())
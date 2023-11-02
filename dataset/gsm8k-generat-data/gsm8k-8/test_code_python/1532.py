def solution():
    # Define the initial number of nails
    initial_nails = 400

    # Calculate the number of nails used in the kitchen
    nails_used_kitchen = 0.3 * initial_nails

    # Calculate the remaining number of nails after fixing the kitchen
    remaining_nails_1 = initial_nails - nails_used_kitchen

    # Calculate the number of nails used in the fence
    nails_used_fence = 0.7 * remaining_nails_1

    # Calculate the final number of remaining nails
    remaining_nails_2 = remaining_nails_1 - nails_used_fence
    result = remaining_nails_2
    return result

print(solution())
def solution():
    """A fixer uses 30% of the nails in a container to repair the kitchen. He also used 70% of the remaining nails in the container to repair the fence. If there were 400 nails in the container, how many nails are remaining?"""
    # Define the initial number of nails
    initial_nails = 400

    # Calculate the number of nails used to repair the kitchen
    kitchen_nails = initial_nails * 0.3

    # Calculate the number of remaining nails after repairing the kitchen
    remaining_nails = initial_nails - kitchen_nails

    # Calculate the number of nails used to repair the fence
    fence_nails = remaining_nails * 0.7

    # Calculate the number of remaining nails
    remaining_nails = remaining_nails - fence_nails

    # return the result
    result = remaining_nails
    return result

print(solution())
def solution():
    """Tim has 22 cans of soda. Jeff comes by, and takes 6 cans of soda from Tim. Tim then goes and buys another half the amount of soda cans he had left. How many cans of soda does Tim have in the end?"""
    # Define the initial number of soda cans Tim has
    initial_cans = 22

    # Subtract the cans taken by Jeff
    cans_left = initial_cans - 6

    # Calculate the number of cans Tim buys
    cans_bought = cans_left / 2

    # Calculate the total number of cans Tim has in the end
    total_cans = cans_left + cans_bought

    # Display the total number of cans Tim has in the end
    result = total_cans
    return result

print(solution())
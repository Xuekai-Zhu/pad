def solution():
    """Brenda catches smallpox. She has 60 blisters on each arm and 80 blisters on the rest of her body. How many blisters does she have in total?"""
    # Define the number of blisters on each arm and the rest of the body
    arm_blisters = 60
    rest_blisters = 80

    # Calculate the total number of blisters
    total_blisters = (2 * arm_blisters) + rest_blisters

    # Return the result
    result = total_blisters
    return result

print(solution())
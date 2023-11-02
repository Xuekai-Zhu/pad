def solution():
    """After Martha went grocery shopping she had 4 bottles of juice in the refrigerator and 4 bottles in the pantry. During the week Martha bought 5 more bottles of juice. If Martha and her family drank 3 bottles of juice during the week, how many bottles are left?"""
    # Define the initial number of bottles
    initial_bottles = 8

    # Define the number of bottles bought during the week
    bought_bottles = 5

    # Define the number of bottles drunk during the week
    drunk_bottles = 3

    # Calculate the number of bottles left
    bottles_left = initial_bottles + bought_bottles - drunk_bottles

    # Return the result
    result = bottles_left
    return result

print(solution())
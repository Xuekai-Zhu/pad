def solution():
    """After Martha went grocery shopping she had 4 bottles of juice in the refrigerator and 4 bottles in the pantry. During the week Martha bought 5 more bottles of juice. If Martha and her family drank 3 bottles of juice during the week, how many bottles are left?"""
    # Define the initial number of bottles of juice
    initial_juice = 4 + 4

    # Define the number of bottles of juice bought during the week
    bought_juice = 5

    # Define the number of bottles of juice drank during the week
    drank_juice = 3

    # Calculate the number of bottles of juice left
    left_juice = initial_juice + bought_juice - drank_juice

    # Display the number of bottles of juice left
    result = left_juice
    return result

print(solution())
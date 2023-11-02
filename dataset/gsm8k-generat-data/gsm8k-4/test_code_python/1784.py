def solution():
    """Nancy has a bag containing 22 tortilla chips. She gives 7 tortilla chips to her brother and 5 tortilla chips to her sister, keeping the rest for herself. How many did Nancy keep for herself?"""
    # Define the initial number of tortilla chips
    initial_chips = 22

    # Define the number of chips given to brother and sister
    chips_given = 7 + 5

    # Calculate the number of chips kept by Nancy
    chips_kept = initial_chips - chips_given

    result = chips_kept
    return result

print(solution())
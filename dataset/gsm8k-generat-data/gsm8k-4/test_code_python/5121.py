def solution():
    """Andrea needs 45 rhinestones to finish an art project. She bought a third of what she needed and found a fifth of what she needed in her supplies. How many rhinestones does she still need?"""
    # Define the total number of rhinestones needed
    total_rhinestones = 45

    # Calculate the number of rhinestones Andrea bought
    bought_rhinestones = total_rhinestones / 3

    # Calculate the number of rhinestones Andrea found in her supplies
    found_rhinestones = total_rhinestones / 5

    # Calculate the number of rhinestones Andrea still needs
    still_needs_rhinestones = total_rhinestones - bought_rhinestones - found_rhinestones

    # return the result
    result = still_needs_rhinestones
    return result

print(solution())
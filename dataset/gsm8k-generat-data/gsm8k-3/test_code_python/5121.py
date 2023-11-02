def solution():
    """Andrea needs 45 rhinestones to finish an art project. She bought a third of what she needed and found a fifth of what she needed in her supplies. How many rhinestones does she still need?"""
    # Define the total number of rhinestones Andrea needs
    total_needed = 45

    # Calculate the number of rhinestones Andrea bought
    bought = total_needed // 3

    # Calculate the number of rhinestones Andrea found in her supplies
    found = total_needed // 5

    # Calculate the total number of rhinestones Andrea still needs
    still_needed = total_needed - bought - found

    # Display the number of rhinestones Andrea still needs
    result = still_needed
    return result

print(solution())
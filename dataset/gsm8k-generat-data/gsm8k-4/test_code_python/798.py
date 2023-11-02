def solution():
    """Patsy is gearing up for this weekend’s graduation. She needs to have 6 appetizers per each of her 30 guests. She’s making 3 dozen deviled eggs, 2 dozen pigs in a blanket and 2 dozen kebabs. How many more dozen appetizers does she need to make?"""
    # Define the number of guests and the required number of appetizers per guest
    guests = 30
    appetizers_per_guest = 6

    # Calculate the total number of required appetizers
    total_appetizers = guests * appetizers_per_guest

    # Calculate the number of appetizers Patsy already made
    deviled_eggs = 3 * 12
    pigs_in_a_blanket = 2 * 12
    kebabs = 2 * 12
    total_appetizers_made = deviled_eggs + pigs_in_a_blanket + kebabs

    # Calculate the number of appetizers she still needs to make
    appetizers_left = total_appetizers - total_appetizers_made

    # Convert the number of appetizers left to dozens
    dozens_left = appetizers_left / 12

    result = dozens_left
    return result

print(solution())
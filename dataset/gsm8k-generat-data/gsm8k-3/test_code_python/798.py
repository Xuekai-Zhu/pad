def solution():
    """Patsy is gearing up for this weekend’s graduation.  She needs to have 6 appetizers per each of her 30 guests.  She’s making 3 dozen deviled eggs, 2 dozen pigs in a blanket and 2 dozen kebabs.  How many more dozen appetizers does she need to make?"""
    # Define the number of guests and appetizers needed per guest
    num_guests = 30
    appetizers_per_guest = 6

    # Define the number of each type of appetizer already made
    deviled_eggs = 3 * 12
    pigs_in_blanket = 2 * 12
    kebabs = 2 * 12

    # Calculate the total number of appetizers needed
    total_appetizers_needed = num_guests * appetizers_per_guest

    # Calculate the total number of appetizers already made
    total_appetizers_made = deviled_eggs + pigs_in_blanket + kebabs

    # Calculate the number of additional appetizers needed
    additional_appetizers_needed = total_appetizers_needed - total_appetizers_made
    additional_appetizers_needed_dozens = additional_appetizers_needed / 12

    # Display the number of additional appetizers needed in dozens
    result = additional_appetizers_needed_dozens
    return result

print(solution())
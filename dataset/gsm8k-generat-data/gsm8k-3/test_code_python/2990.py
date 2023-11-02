def solution():
    """A dragon hoards jewels and gold in its cave. A jealous king snuck in and stole three prize jewels. The dragon burned him to a crisp and stole back its jewels, along with twice as many of the king’s crown jewels from his crown that melted in the dragon’s fire. The new jewels were a third of the number of jewels the dragon had owned before. How many jewels did the dragon own in the end?"""
    # Define the number of jewels stolen by the king and the multiplier for the number of new jewels gained
    STOLEN_JEWELS = 3
    NEW_JEWELS_MULTIPLIER = 2/3

    # Calculate the number of original jewels the dragon had
    original_jewels = (STOLEN_JEWELS / NEW_JEWELS_MULTIPLIER)

    # Calculate the total number of jewels the dragon has at the end
    total_jewels = original_jewels + (2 * STOLEN_JEWELS)

    # Display the total number of jewels
    result = total_jewels
    return result

print(solution())
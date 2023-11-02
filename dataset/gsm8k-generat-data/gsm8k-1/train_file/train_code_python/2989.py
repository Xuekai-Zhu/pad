def solution():
    """A dragon hoards jewels and gold in its cave. A jealous king snuck in and stole three prize jewels. The dragon burned him to a crisp and stole back its jewels, along with twice as many of the king’s crown jewels from his crown that melted in the dragon’s fire. The new jewels were a third of the number of jewels the dragon had owned before. How many jewels did the dragon own in the end?"""

    # Number of jewels the dragon had before the theft
    initial_jewels = (3 + 2*3)*3

    # Number of jewels returned (original 3 plus 2*3 from crown)
    returned_jewels = 3 + 2*3

    # New total number of jewels
    total_jewels = initial_jewels + returned_jewels

    # New number of jewels after the new ones are a third of the original count
    final_jewels = total_jewels / (1 + (1/3))

    return final_jewels

print(solution())
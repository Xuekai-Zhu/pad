def solution():
    """A dragon hoards jewels and gold in its cave. A jealous king snuck in and stole three prize jewels. The dragon burned him to a crisp and stole back its jewels, along with twice as many of the king’s crown jewels from his crown that melted in the dragon’s fire. The new jewels were a third of the number of jewels the dragon had owned before. How many jewels did the dragon own in the end?"""
    initial_jewels = 3
    stolen_jewels = 3
    additional_jewels = 2 * stolen_jewels
    total_jewels = (initial_jewels + additional_jewels) / (1/3)
    result = total_jewels
    return result

print(solution())
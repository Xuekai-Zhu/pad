def solution():
    """A dragon hoards jewels and gold in its cave. A jealous king snuck in and stole three prize jewels. The dragon burned him to a crisp and stole back its jewels, along with twice as many of the king’s crown jewels from his crown that melted in the dragon’s fire. The new jewels were a third of the number of jewels the dragon had owned before. How many jewels did the dragon own in the end?"""
    #Represent the number of jewels the dragon had before as x
    x = None

    #When the king steals 3 jewels, the dragon is left with (x-3) jewels
    x = x - 3

    #The dragon then takes twice as many of the melted crown jewels, which is 2*(3 jewels), or 6 jewels
    x += 6

    #The new total number of jewels is a third of the original number, which means x/3 is equal to the new total number of jewels.
    #Solve for x to find the original number of jewels the dragon had.
    x *= 3

    result = x
    return result

print(solution())
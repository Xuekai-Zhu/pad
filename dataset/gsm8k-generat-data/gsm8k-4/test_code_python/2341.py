def solution():
    """Bill and Ted head to the river to throw stuff into the water. Bill throws 6 more sticks into the river than Ted does, but Ted tosses twice as many rocks into the river as Bill. If Ted tosses 10 sticks and 10 rocks into the river, how many objects did Bill toss into the river?"""
    # Define the number of rocks and sticks Ted threw
    ted_rocks = 10
    ted_sticks = 10

    # Calculate the number of sticks Bill threw
    bill_sticks = ted_sticks + 6

    # Calculate the number of rocks Bill threw
    bill_rocks = ted_rocks / 2

    # Calculate the total number of objects Bill threw
    bill_total = bill_rocks + bill_sticks

    result = bill_total
    return result

print(solution())
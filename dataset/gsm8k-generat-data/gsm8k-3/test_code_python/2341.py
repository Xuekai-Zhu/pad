def solution():
    """Bill and Ted head to the river to throw stuff into the water. Bill throws 6 more sticks into the river than Ted does, but Ted tosses twice as many rocks into the river as Bill. If Ted tosses 10 sticks and 10 rocks into the river, how many objects did Bill toss into the river?"""
    # Define Ted's number of sticks and rocks
    ted_sticks = 10
    ted_rocks = 10

    # Calculate Bill's number of sticks and rocks based on Ted's numbers
    bill_sticks = ted_sticks + 6
    bill_rocks = ted_rocks/2

    # Calculate Bill's total number of objects tossed into the river
    bill_total = bill_sticks + bill_rocks

    # Display Bill's total number of objects
    result = bill_total
    return result

print(solution())
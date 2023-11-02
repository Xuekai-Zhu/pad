def solution():
    """Bill and Ted head to the river to throw stuff into the water. Bill throws 6 more sticks into the river than Ted does, but Ted tosses twice as many rocks into the river as Bill. If Ted tosses 10 sticks and 10 rocks into the river, how many objects did Bill toss into the river?"""
    ted_sticks = 10
    ted_rocks = 10
    bill_sticks = ted_sticks + 6
    bill_rocks = bill_sticks / 2
    total_objects = ted_sticks + ted_rocks + bill_sticks + bill_rocks
    result = total_objects
    return result

print(solution())
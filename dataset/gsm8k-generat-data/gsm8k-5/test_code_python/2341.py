def solution():
    ted_sticks = 10  # Ted tosses 10 sticks into the river
    ted_rocks = 10  # Ted tosses 10 rocks into the river
    bill_sticks = ted_sticks - 6  # Bill throws 6 more sticks than Ted
    bill_rocks = bill_sticks / 2  # Ted throws twice as many rocks as sticks

    # Calculate the total number of objects Bill throws into the river
    total_objects = bill_sticks + bill_rocks
    result = total_objects
    return result

print(solution())
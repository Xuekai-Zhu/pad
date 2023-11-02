def solution():
    ted_sticks = 10
    ted_rocks = 10

    # Ted throws twice as many rocks as Bill
    bill_rocks = ted_rocks / 2

    # Bill throws 6 more sticks than Ted
    bill_sticks = ted_sticks + 6

    # Calculate the total number of objects Bill threw into the river
    total_objects = bill_sticks + bill_rocks
    result = total_objects
    return result

print(solution())
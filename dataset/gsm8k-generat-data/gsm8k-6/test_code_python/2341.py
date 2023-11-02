def solution():
    # Calculate the number of sticks Bill and Ted each threw
    ted_sticks = 10
    bill_sticks = ted_sticks - 6
    # Calculate the number of rocks Bill and Ted each threw
    ted_rocks = 10
    bill_rocks = ted_rocks / 2
    # Calculate the total number of objects Bill threw into the river
    total_objects = bill_sticks + bill_rocks
    result = total_objects
    return result

print(solution())
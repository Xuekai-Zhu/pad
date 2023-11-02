def solution():
    # Define the number of rocks Ted throws
    ted_rocks = 10

    # Define the number of sticks Ted throws
    ted_sticks = 10

    # Calculate the number of sticks Bill throws
    bill_sticks = ted_sticks + 6

    # Calculate the number of rocks Bill throws
    bill_rocks = ted_rocks / 2

    # Calculate the total number of objects Bill throws
    bill_objects = bill_sticks + bill_rocks

    result = bill_objects
    return result

print(solution())
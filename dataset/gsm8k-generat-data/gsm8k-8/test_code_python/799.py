def solution():
    # Calculate the total number of legs on the tables and chairs with 4 legs each
    four_legs = 4 * 2 + 1 * 4 + 2 * 4

    # Calculate the total number of legs on the tables with 3 legs each
    three_legs = 3 * 3

    # Calculate the total number of legs on the table with 1 leg and the rocking chair
    other_legs = 1 + 2 * 2

    # Calculate the total number of legs in the room
    total_legs = four_legs + three_legs + other_legs

    result = total_legs
    return result

print(solution())
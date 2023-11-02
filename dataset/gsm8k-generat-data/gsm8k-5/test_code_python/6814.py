def solution():
    # Number of people on the first bus
    first_bus = 12

    # Number of people on the second bus (twice the number on the first)
    second_bus = 2 * first_bus

    # Number of people on the third bus (6 fewer than the second bus)
    third_bus = second_bus - 6

    # Number of people on the fourth bus (9 more than the first bus)
    fourth_bus = first_bus + 9

    # Total number of people going to the museum
    total_people = first_bus + second_bus + third_bus + fourth_bus
    result = total_people
    return result

print(solution())
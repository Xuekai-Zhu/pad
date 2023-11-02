def solution():
    first_bus = 12
    second_bus = first_bus * 2
    third_bus = second_bus - 6
    fourth_bus = first_bus + 9

    # Calculate the total number of people on all buses
    total_people = first_bus + second_bus + third_bus + fourth_bus
    result = total_people
    return result

print(solution())
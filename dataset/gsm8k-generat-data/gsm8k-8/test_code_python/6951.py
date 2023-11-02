def solution():
    # Let x be the total amount of storage space on the second floor
    x = 5000 * 4

    # Let y be the total amount of storage space on the first floor
    y = 2 * x

    # The total amount of storage space in the warehouse is x + y
    total_space = x + y

    # The amount of space used on the first floor is y
    space_used_on_first_floor = y

    # The amount of space available in the building is the total space minus the space used
    space_available = total_space - space_used_on_first_floor
    result = space_available
    return result

print(solution())
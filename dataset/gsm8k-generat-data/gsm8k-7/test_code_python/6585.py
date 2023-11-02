def solution():
    carrying_capacity = 80

    # Calculate the number of people who entered the bus at the first pickup point
    first_pickup = carrying_capacity * 3 / 5

    # Calculate the number of people who will be on the bus after the first pickup
    total_on_bus = first_pickup + 50

    # Calculate the number of people who could not take the bus because it was full
    number_left_behind = carrying_capacity - total_on_bus
    result = number_left_behind
    return result

print(solution())
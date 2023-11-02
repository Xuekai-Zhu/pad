def solution():
    # Define the carrying capacity of the bus
    carrying_capacity = 80

    # Calculate the number of people who entered the bus at the first pickup point
    first_pickup = 3/5 * carrying_capacity

    # Calculate the total number of passengers on the bus after the first pickup
    total_passengers = first_pickup + 50

    # Calculate the number of people who could not take the bus because it was full
    not_on_bus = total_passengers - carrying_capacity
    result = not_on_bus
    return result

print(solution())
def solution():
    carrying_capacity = 80  # The carrying capacity of the bus is 80 people
    first_pickup = carrying_capacity * 3/5  # The number of people who entered the bus at the first pickup point
    total_passengers = first_pickup + 50  # The total number of people on the bus after the second pickup point

    # Calculate the number of people who could not take the bus because it was full
    full_capacity = carrying_capacity
    excess_passengers = total_passengers - full_capacity
    result = excess_passengers
    return result

print(solution())
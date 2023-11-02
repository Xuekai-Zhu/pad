def solution():
    carrying_capacity = 80  # carrying capacity of the bus
    first_pickup = 3/5 * carrying_capacity  # number of people who entered the bus at the first pickup point
    total_people = first_pickup + 50  # total number of people at the second pickup point
    remaining_capacity = carrying_capacity - first_pickup  # remaining capacity after the first pickup
    not_taken = max(0, total_people - carrying_capacity)  # number of people who could not take the bus because it was full
    result = not_taken
    return result

print(solution())
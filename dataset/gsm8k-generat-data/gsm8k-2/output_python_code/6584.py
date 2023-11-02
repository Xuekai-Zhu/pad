def solution():
    """A bus has a carrying capacity of 80 people. At the first pickup point, the number of people who entered the bus was 3/5 of its carrying capacity. If there were 50 people at the next pick-up point, how many people could not take the bus because it was full?"""
    carrying_capacity = 80
    first_pickup = 3 / 5 * carrying_capacity
    current_capacity = first_pickup + 50
    people_left_behind = max(0, current_capacity - carrying_capacity)
    result = people_left_behind
    return result

print(solution())
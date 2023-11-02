def solution():
    """Stella and Twinkle are filling up a truck with a capacity of 6000 stone blocks at the rate of 250 blocks per hour per person.
    They work for four hours and are then joined by 6 other people who also work at the same rate. How many hours did filling the truck take?"""
    truck_capacity = 6000
    rate_per_person_per_hour = 250
    initial_number_of_people = 2
    initial_time_worked = 4
    additional_people = 6
    total_people = initial_number_of_people + additional_people
    total_time = initial_time_worked + (truck_capacity / (rate_per_person_per_hour * total_people))
    result = total_time
    return result

print(solution())
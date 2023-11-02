def solution():
    garbage_per_collection = 200
    collections_per_week = 3
    weeks_without_pickup = 2

    # Calculate the total amount of garbage generated in 2 weeks
    total_garbage_generated = garbage_per_collection * collections_per_week * weeks_without_pickup

    # During the first week, additional garbage is piled up
    # During the second week, the amount of garbage is halved
    total_garbage_accumulated = total_garbage_generated + (total_garbage_generated / 2)

    result = total_garbage_accumulated
    return result

print(solution())
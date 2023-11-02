def solution():
    """Carson is a night security guard. He's supposed to patrol the outside of a warehouse that's 600 feet long and 400 feet wide. If Carson is supposed to circle the warehouse 10 times, but gets tired and skips 2 times, how far does he walk in one night?"""
    warehouse_length = 600
    warehouse_width = 400
    num_patrols = 10
    skipped_patrols = 2
    total_distance = (2 * warehouse_length) + (2 * warehouse_width)
    distance_per_patrol = total_distance * num_patrols - (skipped_patrols * total_distance)
    result = distance_per_patrol
    return result

print(solution())
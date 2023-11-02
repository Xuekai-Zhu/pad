def solution():
    """Carson is a night security guard. He's supposed to patrol the outside of a warehouse that's 600 feet long and 400 feet wide. If Carson is supposed to circle the warehouse 10 times, but gets tired and skips 2 times, how far does he walk in one night?"""
    length = 600
    width = 400
    perimeter = 2 * (length + width)
    times_patrolled = 10 - 2
    total_distance = perimeter * times_patrolled
    result = total_distance
    return result

print(solution())
def solution():
    """Mary's sheep can run 12 feet per second, and her sheepdog can run 20 feet per second. A sheep standing 160 feet away from the sheep dog bolts, and the dog runs after it. How many seconds does it take the dog to catch the sheep?"""
    sheep_speed = 12
    dog_speed = 20
    distance = 160
    relative_speed = dog_speed - sheep_speed
    time_to_catch = distance / relative_speed
    result = time_to_catch
    return result

print(solution())
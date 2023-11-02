def solution():
    """Ivan has a bird feeder in his yard that holds two cups of birdseed. Every week, he has to refill the emptied feeder. Each cup of birdseed can feed fourteen birds, but Ivan is constantly chasing away a hungry squirrel that steals half a cup of birdseed from the feeder every week. How many birds does Ivan’s bird feeder feed weekly?"""
    feeder_capacity = 2
    birds_per_cup = 14
    squirrel_steal = 0.5
    remaining_birdseed = feeder_capacity - squirrel_steal
    birds_per_week = remaining_birdseed * birds_per_cup
    result = birds_per_week
    return result

print(solution())
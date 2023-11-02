def solution():
    """Ivan has a bird feeder in his yard that holds two cups of birdseed. Every week, he has to refill the emptied feeder. Each cup of birdseed can feed fourteen birds, but Ivan is constantly chasing away a hungry squirrel that steals half a cup of birdseed from the feeder every week. How many birds does Ivan’s bird feeder feed weekly?"""
    birdseed_capacity = 2
    birdseed_needed = 1
    birds_per_cup = 14
    squirrel_steals = 0.5
    birdseed_per_week = birdseed_capacity - squirrel_steals
    total_birds = birdseed_per_week * birds_per_cup
    result = total_birds
    return result

print(solution())
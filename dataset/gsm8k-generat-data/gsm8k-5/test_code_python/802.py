def solution():
    feeder_capacity = 2  # The feeder holds 2 cups of birdseed
    birds_per_cup = 14  # Each cup of birdseed can feed 14 birds
    squirrel_theft = 0.5  # The squirrel steals 0.5 cups of birdseed every week

    # Calculate the amount of birdseed that Ivan's feeder can provide each week, after accounting for the thief squirrel
    effective_feeder_capacity = feeder_capacity - squirrel_theft
    birdseed_per_week = effective_feeder_capacity * birds_per_cup

    # Calculate the number of birds that can be fed from the birdseed available each week
    birds_per_week = birdseed_per_week * birds_per_cup
    result = birds_per_week
    return result

print(solution())
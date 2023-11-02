def solution():
    # Calculate the total amount of birdseed available for the birds
    total_birdseed = 2  # the bird feeder holds two cups of birdseed
    available_birdseed = total_birdseed - 0.5  # the squirrel steals half a cup of birdseed every week

    # Calculate the number of birds that can be fed by the available birdseed
    birds_fed = available_birdseed * 14  # each cup of birdseed can feed fourteen birds

    result = birds_fed
    return result

print(solution())
def solution():
    """Ivan has a bird feeder in his yard that holds two cups of birdseed. Every week, he has to refill the emptied feeder. Each cup of birdseed can feed fourteen birds, but Ivan is constantly chasing away a hungry squirrel that steals half a cup of birdseed from the feeder every week. How many birds does Ivan’s bird feeder feed weekly?"""
    # Define the amount of birdseed in the feeder
    birdseed = 2

    # Calculate the amount of birdseed left after the squirrel steals some
    birdseed -= 0.5

    # Calculate the total number of birds that can be fed with the remaining birdseed
    bird_count = birdseed * 14

    # Return the result
    result = bird_count
    return result

print(solution())
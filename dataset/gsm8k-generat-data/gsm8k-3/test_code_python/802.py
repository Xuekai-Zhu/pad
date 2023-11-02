def solution():
    """Ivan has a bird feeder in his yard that holds two cups of birdseed. Every week, he has to refill the emptied feeder. Each cup of birdseed can feed fourteen birds, but Ivan is constantly chasing away a hungry squirrel that steals half a cup of birdseed from the feeder every week. How many birds does Ivan’s bird feeder feed weekly?"""
    # Define the number of cups of birdseed in the feeder
    cups_of_birdseed = 2

    # Define the number of birds that can be fed by one cup of birdseed
    birds_per_cup = 14

    # Define the amount of birdseed stolen by the squirrel every week
    stolen_birdseed = 0.5

    # Calculate the total amount of birdseed available for the birds
    available_birdseed = cups_of_birdseed - stolen_birdseed

    # Calculate the total number of birds that can be fed
    total_birds = available_birdseed * birds_per_cup

    # Display the total number of birds that can be fed
    result = total_birds
    return result

print(solution())
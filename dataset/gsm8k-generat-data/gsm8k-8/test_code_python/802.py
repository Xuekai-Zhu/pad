def solution():
    # Define amount of birdseed in the feeder and amount stolen by the squirrel each week
    birdseed = 2
    squirrel_steal = 0.5

    # Calculate amount of birdseed available after squirrel steals
    birdseed_left = birdseed - squirrel_steal

    # Calculate number of birds that can be fed with the remaining birdseed
    birds_fed = birdseed_left * 14

    result = birds_fed
    return result

print(solution())
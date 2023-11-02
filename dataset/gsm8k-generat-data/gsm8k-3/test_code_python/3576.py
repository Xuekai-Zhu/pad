def solution():
    """Billy and Margaret are competing with each other to see who can swim 10 laps the fastest. Billy swims his first 5 laps in 2 minutes, swims the next 3 laps in 4 minutes, swims the next lap in 1 minute, then swims his final lap. Margaret finishes swimming all of her laps in 10 minutes. Billy wins the competition by finishing his laps 30 seconds before Margaret does. In seconds, how long did it take Billy to swim his final lap?"""
    # Define the number of laps and times for Billy and Margaret
    billy_laps = 10
    billy_time = 0
    margaret_laps = 10
    margaret_time = 600

    # Calculate Billy's time for the first 5 laps
    billy_time += 2 * 60

    # Calculate Billy's time for the next 3 laps
    billy_time += 4 * 60

    # Calculate Billy's time for the next lap
    billy_time += 1 * 60

    # Calculate Billy's time for the final lap
    billy_time += (margaret_time - billy_time - 30) / (billy_laps - 9)

    # Display Billy's time for the final lap in seconds
    result = billy_time - 9 * 60
    return result

print(solution())
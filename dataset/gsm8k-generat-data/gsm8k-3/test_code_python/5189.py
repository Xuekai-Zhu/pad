def solution():
    """4 friends are running a 4 x 100 relay race.  Mary ran first and took twice as long as Susan.  Susan ran second and she took 10 seconds longer than Jen.  Jen ran third and finished in 30 seconds.  Tiffany ran the last leg and finished in 7 seconds less than Mary.  How many seconds did it take the team to finish the race?"""
    # Define the time taken by each runner
    mary_time = 0
    susan_time = 0
    jen_time = 30
    tiffany_time = 0

    # Calculate Susan's time
    susan_time = jen_time + 10

    # Calculate Mary's time
    mary_time = susan_time * 2 - 7

    # Calculate the total time taken
    total_time = mary_time + susan_time + jen_time + tiffany_time

    # Display the total time taken
    result = total_time
    return result

print(solution())
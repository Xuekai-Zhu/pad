def solution():
    """4 friends are running a 4 x 100 relay race. Mary ran first and took twice as long as Susan. Susan ran second and she took 10 seconds longer than Jen. Jen ran third and finished in 30 seconds. Tiffany ran the last leg and finished in 7 seconds less than Mary. How many seconds did it take the team to finish the race?"""
    # Define the times for each person
    mary_time = None
    susan_time = None
    jen_time = 30
    tiffany_time = None

    # Calculate Mary's time based on her relationship with Susan's time
    susan_time = jen_time + 10
    mary_time = 2 * susan_time

    # Calculate Tiffany's time based on her relationship with Mary's time
    tiffany_time = mary_time - 7

    # Calculate the total time for the team
    total_time = mary_time + susan_time + jen_time + tiffany_time

    # return the result
    result = total_time
    return result

print(solution())
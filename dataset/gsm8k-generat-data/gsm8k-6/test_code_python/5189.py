def solution():
    # Calculate the time taken by each runner
    mary_time = 2 * susan_time  # Mary took twice as long as Susan
    susan_time = jen_time + 10  # Susan took 10 seconds longer than Jen
    jen_time = 30  # Jen finished in 30 seconds
    tiffany_time = mary_time - 7  # Tiffany finished 7 seconds faster than Mary

    # Calculate the total time taken by the team
    total_time = mary_time + susan_time + jen_time + tiffany_time

    result = total_time
    return result

print(solution())
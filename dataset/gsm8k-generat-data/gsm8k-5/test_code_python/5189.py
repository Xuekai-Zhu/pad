def solution():
    # Time taken by Mary
    mary_time = 2 * susan_time  # Mary took twice as long as Susan

    # Time taken by Susan
    susan_time = jen_time + 10  # Susan took 10 seconds longer than Jen

    # Time taken by Jen
    jen_time = 30  # Jen finished in 30 seconds

    # Time taken by Tiffany
    tiffany_time = mary_time - 7  # Tiffany finished 7 seconds before Mary

    # Total time taken by the team
    total_time = mary_time + susan_time + jen_time + tiffany_time
    result = total_time
    return result

print(solution())
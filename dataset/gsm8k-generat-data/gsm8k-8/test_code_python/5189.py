def solution():
    # Define the times for each runner
    mary_time = 2 * susan_time
    susan_time = jen_time + 10
    jen_time = 30
    tiffany_time = mary_time - 7

    # Calculate the total time for the team
    total_time = mary_time + susan_time + jen_time + tiffany_time
    result = total_time
    return result

print(solution())
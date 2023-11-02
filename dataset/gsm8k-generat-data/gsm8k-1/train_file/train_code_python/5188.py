def solution():
    """4 friends are running a 4 x 100 relay race. Mary ran first and took twice as long as Susan. Susan ran second and she took 10 seconds longer than Jen. Jen ran third and finished in 30 seconds. Tiffany ran the last leg and finished in 7 seconds less than Mary. How many seconds did it take the team to finish the race?"""
    mary_time = 2 * susan_time
    susan_time = jen_time + 10
    jen_time = 30
    tiffany_time = mary_time - 7
    
    total_time = mary_time + susan_time + jen_time + tiffany_time
    result = total_time
    return result

print(solution())
def solution():
    mary_time = 60  # assume Mary took 60 seconds
    susan_time = mary_time / 2
    jen_time = susan_time + 10
    tiffany_time = mary_time - 7

    total_time = mary_time + susan_time + jen_time + tiffany_time
    result = total_time
    return result

print(solution())
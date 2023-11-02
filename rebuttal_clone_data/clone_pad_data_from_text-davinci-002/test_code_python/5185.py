def solution():
    times_fishing = 5
    shelly_catch = times_fishing * 5 - 2
    sam_catch = shelly_catch - 1 
    total_catch = shelly_catch + sam_catch
    return total_catch

print(solution())
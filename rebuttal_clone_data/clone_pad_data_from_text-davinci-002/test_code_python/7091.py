def solution():
    bikes_sold_morning = 19
    bikes_sold_afternoon = 27
    clamps_per_bike = 2
    total_clamps = (bikes_sold_morning + bikes_sold_afternoon) * clamps_per_bike
    result = total_clamps
    return result

print(solution())
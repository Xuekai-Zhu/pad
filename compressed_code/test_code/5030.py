def solution():
    
    hourly_catch = 7
    hours_fished = 9
    lost_fish = 15
    total_catch = (hourly_catch * hours_fished) - lost_fish
    result = total_catch
    return result

print(solution())
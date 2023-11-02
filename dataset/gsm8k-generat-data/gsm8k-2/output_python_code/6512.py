def solution():
    """Julio goes fishing and can catch 7 fish every hour. By the 9th hour, how many fish does Julio have if he loses 15 fish in the process?"""
    hourly_catch = 7
    hours_fished = 9
    lost_fish = 15
    total_catch = (hourly_catch * hours_fished) - lost_fish
    result = total_catch
    return result

print(solution())
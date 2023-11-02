def solution():
    """Julio goes fishing and can catch 7 fish every hour. By the 9th hour, how many fish does Julio have if he loses 15 fish in the process?"""
    fish_per_hour = 7
    hours_fishing = 9
    fish_lost = 15
    total_fish = (fish_per_hour * hours_fishing) - fish_lost
    result = total_fish
    return result

print(solution())
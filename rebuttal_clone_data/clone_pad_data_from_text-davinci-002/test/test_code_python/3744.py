def solution():
    minutes_per_flower = 10
    time_gathering = 2
    flowers_needed = 30
    flowers_gathered = time_gathering * 60 / minutes_per_flower
    flowers_lost = 3
    flowers_remaining = flowers_needed - flowers_gathered + flowers_lost
    minutes_remaining = flowers_remaining * minutes_per_flower
    result = minutes_remaining
    return result

print(solution())
def solution():
    potatoes_eaten = 3
    potatoes_total = 27
    minutes_elapsed = 20
    minutes_in_an_hour = 60
    hours_elapsed = minutes_elapsed / minutes_in_an_hour
    potatoes_per_hour = potatoes_eaten / hours_elapsed
    hours_to_eat_all_potatoes = potatoes_total / potatoes_per_hour
    result = hours_to_eat_all_potatoes
    return result

print(solution())
def solution():
    
    trip_freq = 0.4
    drop_coffee_freq = 0.25 * trip_freq
    not_drop_coffee_freq = 1 - drop_coffee_freq
    result = not_drop_coffee_freq * 100
    return result

print(solution())
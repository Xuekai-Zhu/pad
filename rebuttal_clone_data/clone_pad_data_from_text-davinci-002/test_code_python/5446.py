def solution():
    floors = 10
    even_floors = floors / 2
    odd_floors = (floors - even_floors)
    seconds_per_even_floor = 15
    seconds_per_odd_floor = 9
    total_seconds = (even_floors * seconds_per_even_floor) + (odd_floors * seconds_per_odd_floor)
    minutes = total_seconds / 60
    result = minutes
    return result

print(solution())
def solution():
    
    floors = 12
    full_floors = floors / 2
    half_capacity_floors = floors - full_floors
    total_apartments = (full_floors * 10) + (half_capacity_floors * 10 / 2)
    total_people = total_apartments * 4
    result = total_people
    return result

print(solution())
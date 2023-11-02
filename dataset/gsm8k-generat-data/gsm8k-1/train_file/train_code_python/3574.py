def solution():
    """An apartment building has 12 floors and half of them are full. The remaining floors are all at half-capacity. If each floor has 10 apartments and each apartment has four people, how many people are in the building?"""
    floors = 12
    full_floors = floors / 2
    half_capacity_floors = floors - full_floors
    total_apartments = (full_floors * 10) + (half_capacity_floors * 10 / 2)
    total_people = total_apartments * 4
    result = total_people
    return result

print(solution())
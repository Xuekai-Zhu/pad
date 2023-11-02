def solution():
    """An apartment building has 12 floors and half of them are full. The remaining floors are all at half-capacity. If each floor has 10 apartments and each apartment has four people, how many people are in the building?"""
    total_floors = 12
    full_floors = total_floors / 2
    full_capacity = 10 * 4 * full_floors
    half_capacity = 10 * 2 * 4 * (total_floors - full_floors)
    total_people = full_capacity + half_capacity
    result = total_people
    return result

print(solution())
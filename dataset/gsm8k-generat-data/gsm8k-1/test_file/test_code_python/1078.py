def solution():
    """James decided to walk to the store. When he got halfway there he realized he forgot something at home and had to walk back. If his home is 4 miles from the store and he walks 4 miles per hour how long did it take him to reach the store?"""
    distance = 4
    speed = 4 # miles per hour
    time_to_store = distance / speed
    time_round_trip = time_to_store * 2
    result = time_round_trip
    return result

print(solution())
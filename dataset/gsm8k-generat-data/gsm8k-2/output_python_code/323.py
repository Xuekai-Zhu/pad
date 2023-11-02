def solution():
    """A building has four floors with ten rooms each. Legacy has to clean each room, and it takes her 6 hours to clean one room. If she earns $15 per hour of work, calculate the total amount of money she makes from cleaning all the floors in the building."""
    floors = 4
    rooms_per_floor = 10
    room_time = 6
    hourly_pay = 15
    total_rooms = floors * rooms_per_floor
    total_time = total_rooms * room_time
    total_pay = total_time * hourly_pay
    result = total_pay
    return result

print(solution())
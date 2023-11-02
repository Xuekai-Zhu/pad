def solution():
    """A building has four floors with ten rooms each. Legacy has to clean each room, and it takes her 6 hours to clean one room. If she earns $15 per hour of work, calculate the total amount of money she makes from cleaning all the floors in the building."""
    num_floors = 4
    rooms_per_floor = 10
    hours_per_room = 6
    hourly_rate = 15
    total_rooms = num_floors * rooms_per_floor
    total_hours = total_rooms * hours_per_room
    total_pay = total_hours * hourly_rate
    result = total_pay
    return result

print(solution())
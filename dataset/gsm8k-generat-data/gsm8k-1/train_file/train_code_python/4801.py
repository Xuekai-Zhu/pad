def solution():
    """The battery charge in Mary’s cordless vacuum cleaner lasts ten minutes. It takes her four minutes to vacuum each room in her house. Mary has three bedrooms, a kitchen, and a living room. How many times does Mary need to charge her vacuum cleaner to vacuum her whole house?"""
    battery_life = 10
    time_per_room = 4
    num_rooms = 4
    time_to_clean = time_per_room * num_rooms
    num_charges = time_to_clean // battery_life + 1
    result = num_charges
    return result

print(solution())
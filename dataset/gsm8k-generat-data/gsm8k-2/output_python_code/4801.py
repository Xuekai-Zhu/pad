def solution():
    """The battery charge in Mary’s cordless vacuum cleaner lasts ten minutes. It takes her four minutes to vacuum each room in her house. Mary has three bedrooms, a kitchen, and a living room. How many times does Mary need to charge her vacuum cleaner to vacuum her whole house?"""
    rooms = 4
    time_per_room = 4
    total_time_per_charge = 10
    total_time = rooms * time_per_room
    total_charges = total_time // total_time_per_charge + 1
    result = total_charges
    return result

print(solution())
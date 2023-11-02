def solution():
    floors = 4 # the building has four floors
    rooms_per_floor = 10 # each floor has ten rooms
    rooms_total = floors * rooms_per_floor # calculate the total number of rooms
    hours_per_room = 6 # it takes Legacy 6 hours to clean one room
    hourly_rate = 15 # Legacy earns $15 per hour of work

    # calculate the total amount of time to clean all the rooms
    total_time = rooms_total * hours_per_room

    # calculate the total amount of money earned
    total_earnings = total_time * hourly_rate
    result = total_earnings
    return result

print(solution())
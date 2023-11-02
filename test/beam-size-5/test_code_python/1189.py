def solution():
    
    laundry_cost = 3.00
    room_cost = 1.50
    trash_cost = 0.75
    dishwasher_cost = 0.50
    dishwasher_emptied = 6 * 2
    laundry_earnings = laundry_cost * 2
    room_earnings = room_cost * 2
    trash_earnings = trash_cost * 2
    dishwasher_earnings = dishwasher_emptied * 0.50
    total_earnings = laundry_earnings + room_earnings + trash_earnings + dishwasher_earnings
    result = total_earnings
    return result

print(solution())
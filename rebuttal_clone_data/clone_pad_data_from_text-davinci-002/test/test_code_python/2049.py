def solution():
    minutes_per_room = 3
    minutes_per_dish = 2
    minutes_per_load = 9
    rooms_swept_by_anna = 10
    loads_of_laundry_done_by_billy = 2
    total_minutes_spent_by_anna = minutes_per_room * rooms_swept_by_anna
    total_minutes_spent_by_billy = minutes_per_load * loads_of_laundry_done_by_billy
    dishes_washed_by_billy = (total_minutes_spent_by_anna - total_minutes_spent_by_billy) / minutes_per_dish
    result = dishes_washed_by_billy
    
    return result

print(solution())
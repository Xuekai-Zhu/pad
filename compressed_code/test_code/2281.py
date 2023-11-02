def solution():
    
    initial_money = 17.8
    toy_car_cost = 0.95
    race_track_cost = 6
    toys_cost = 4 * toy_car_cost + race_track_cost
    remaining_money = initial_money - toys_cost
    result = remaining_money
    return result

print(solution())
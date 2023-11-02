def solution():
    """Jude is trading his bottle cap collection to Arthur for some of Arthur's matchbox vehicles. Arthur charges Jude 5 bottle caps for a car and 6 bottle caps for a truck. Jude has 100 bottle caps. If he buys 10 trucks and spends 75% of his remaining bottle caps on cars, how many total matchbox vehicles does he buy?"""
    total_bottle_caps = 100
    trucks_bought = 10
    car_price = 5
    truck_price = 6
    bottle_caps_spent_on_trucks = trucks_bought * truck_price
    remaining_bottle_caps = total_bottle_caps - bottle_caps_spent_on_trucks
    bottle_caps_spent_on_cars = remaining_bottle_caps * 0.75
    cars_bought = bottle_caps_spent_on_cars / car_price
    total_vehicles_bought = trucks_bought + cars_bought
    result = total_vehicles_bought
    return result

print(solution())
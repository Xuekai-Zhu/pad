def solution():
    money_saved = 6000
    flight_cost = 1200
    hotel_cost = 800
    food_cost = 3000
    money_left = money_saved - (flight_cost + hotel_cost + food_cost)
    result = money_left
    return result

print(solution())
def solution():
    savings = 6000
    flight_cost = 1200
    hotel_cost = 800
    food_cost = 3000

    # Calculate the total cost of the trip
    total_cost = flight_cost + hotel_cost + food_cost

    # Calculate how much money Joe has left
    remaining_money = savings - total_cost
    result = remaining_money
    return result

print(solution())
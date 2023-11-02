def solution():
    initial_savings = 6000
    flight_cost = 1200
    hotel_cost = 800
    food_cost = 3000

    total_expenses = flight_cost + hotel_cost + food_cost
    remaining_savings = initial_savings - total_expenses
    result = remaining_savings
    return result

print(solution())
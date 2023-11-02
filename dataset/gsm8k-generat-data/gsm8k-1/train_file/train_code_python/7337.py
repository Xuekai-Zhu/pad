def solution():
    """Joe saves $6,000 for his trip to Australia. If he spends $1,200 on the flight, $800 on a hotel, and $3,000 on food, how much money, in dollars, does he have left?"""
    initial_savings = 6000
    flight_cost = 1200
    hotel_cost = 800
    food_cost = 3000
    total_spent = flight_cost + hotel_cost + food_cost
    money_left = initial_savings - total_spent
    result = money_left
    return result

print(solution())
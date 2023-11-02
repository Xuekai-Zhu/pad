def solution():
    total_savings = 6000  # Joe saves $6,000 for his Australia trip
    flight_cost = 1200  # Joe spends $1,200 on the flight
    hotel_cost = 800  # Joe spends $800 on a hotel
    food_cost = 3000  # Joe spends $3,000 on food

    # Calculate Joe's remaining savings after all expenses
    remaining_savings = total_savings - flight_cost - hotel_cost - food_cost
    result = remaining_savings
    return result

print(solution())
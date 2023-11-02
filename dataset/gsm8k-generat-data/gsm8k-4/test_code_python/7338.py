def solution():
    """Joe saves $6,000 for his trip to Australia. If he spends $1,200 on the flight, $800 on a hotel, and $3,000 on food, how much money, in dollars, does he have left?"""
    # Define the total amount of money saved by Joe
    total_savings = 6000

    # Define the expenses
    flight_expense = 1200
    hotel_expense = 800
    food_expense = 3000

    # Calculate the remaining money
    remaining_money = total_savings - flight_expense - hotel_expense - food_expense

    # return the result
    result = remaining_money
    return result

print(solution())
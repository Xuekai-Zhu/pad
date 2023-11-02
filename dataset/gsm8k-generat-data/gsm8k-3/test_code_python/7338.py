def solution():
    """Joe saves $6,000 for his trip to Australia. If he spends $1,200 on the flight, $800 on a hotel, and $3,000 on food, how much money, in dollars, does he have left?"""
    # Define the amount of money Joe saved
    savings = 6000

    # Define the expenses for the trip
    flight = 1200
    hotel = 800
    food = 3000

    # Calculate the total expenses
    total_expenses = flight + hotel + food

    # Calculate the amount of money Joe has left
    money_left = savings - total_expenses

    # Display the amount of money Joe has left
    result = money_left
    return result

print(solution())
def solution():
    """Ed booked a hotel while he was on vacation. Staying at the hotel cost was $1.50 per hour every night and $2 per hour every morning. If Ed had $80 and he stayed in the hotel for 6 hours last night and 4 hours this morning, how much money was he left with after paying for his stay at the hotel?"""
    # Define the cost per hour for staying at the hotel at night and in the morning
    night_cost = 1.5
    morning_cost = 2

    # Define the number of hours stayed at the hotel at night and in the morning
    night_hours = 6
    morning_hours = 4

    # Calculate the total cost of staying at the hotel
    total_cost = (night_cost * night_hours) + (morning_cost * morning_hours)

    # Calculate the amount of money left after paying for the hotel
    money_left = 80 - total_cost

    # Return the result
    result = money_left
    return result

print(solution())
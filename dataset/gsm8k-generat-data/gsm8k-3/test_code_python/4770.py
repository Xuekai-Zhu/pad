def solution():
    """Ed booked a hotel while he was on vacation. Staying at the hotel cost was $1.50 per hour every night and $2 per hour every morning. If Ed had $80 and he stayed in the hotel for 6 hours last night and 4 hours this morning, how much money was he left with after paying for his stay at the hotel?"""
    # Define the cost per hour for staying at the hotel at night and in the morning
    NIGHT_RATE = 1.5
    MORNING_RATE = 2

    # Calculate the total cost of staying at the hotel
    total_cost = (NIGHT_RATE * 6) + (MORNING_RATE * 4)

    # Calculate the amount of money Ed is left with
    remaining_money = 80 - total_cost

    # Display the remaining amount of money
    result = remaining_money
    return result

print(solution())
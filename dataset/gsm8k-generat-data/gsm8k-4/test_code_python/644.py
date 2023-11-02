def solution():
    """The city’s bus system carries 1,200,000 people each day. How many people does the bus system carry for 13 weeks?"""
    # Define the number of people carried each day
    daily_passengers = 1200000

    # Calculate the number of people carried in 13 weeks (91 days)
    total_passengers = daily_passengers * 91 * 7

    # Return the result
    result = total_passengers
    return result

print(solution())
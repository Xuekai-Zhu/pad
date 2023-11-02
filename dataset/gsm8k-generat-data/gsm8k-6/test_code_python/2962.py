def solution():
    # Calculate Hayden's earnings for driving and giving rides
    earnings_driving = 15 * 8  # $15 per hour for 8 hours
    earnings_rides = 5 * 3  # $5 bonus for each ride, and he gave 3 rides
    bonus_reviews = 2 * 20  # $20 bonus for each good review, and he got 2 good reviews
    total_earnings = earnings_driving + earnings_rides + bonus_reviews  # total earnings for the day

    # Calculate how much Hayden spent on gas
    cost_gas = 17 * 3  # 17 gallons of gas at $3 per gallon

    # Calculate how much Hayden is owed for his work today
    amount_owed = total_earnings - cost_gas
    result = amount_owed
    return result

print(solution())
def solution():
    """An amusement park sells tickets for $3. This week it welcomed 100 people per day but on Saturday it was visited by 200 people and on Sunday by 300. How much money did it make overall in a week?"""
    # Define the ticket price and number of visitors per day for the first 5 days
    ticket_price = 3
    daily_visitors = 100
    total_visitors = daily_visitors * 5

    # Calculate the total earnings from the first 5 days
    earnings_5_days = total_visitors * ticket_price

    # Calculate the earnings from Saturday and Sunday
    earnings_weekend = (200 + 300) * ticket_price

    # Calculate the total earnings for the week
    total_earnings = earnings_5_days + earnings_weekend

    # Display the total earnings
    result = total_earnings
    return result

print(solution())
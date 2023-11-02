def solution():
    """An amusement park sells tickets for $3. This week it welcomed 100 people per day but on Saturday it was visited by 200 people and on Sunday by 300. How much money did it make overall in a week?"""
    ticket_price = 3
    daily_visitors = 100
    weekend_visitors = 200 + 300
    total_visitors = daily_visitors * 5 + weekend_visitors * 2
    total_money = total_visitors * ticket_price
    result = total_money
    return result

print(solution())
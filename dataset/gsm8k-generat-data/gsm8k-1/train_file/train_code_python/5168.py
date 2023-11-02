def solution():
    """An amusement park sells tickets for $3. This week it welcomed 100 people per day but on Saturday it was visited by 200 people and on Sunday by 300. How much money did it make overall in a week?"""
    ticket_price = 3
    daily_visitors = 100
    saturday_visitors = 200
    sunday_visitors = 300
    total_days = 7
    overall_visitors = (daily_visitors * (total_days - 2)) + saturday_visitors + sunday_visitors
    total_income = overall_visitors * ticket_price
    result = total_income
    return result

print(solution())
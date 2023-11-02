def solution():
    """An amusement park sells tickets for $3. This week it welcomed 100 people per day but on Saturday it was visited by 200 people and on Sunday by 300. How much money did it make overall in a week?"""
    # Define the ticket price and the number of visitors
    ticket_price = 3
    visitors_per_day = 100
    saturday_visitors = 200
    sunday_visitors = 300

    # Calculate the total number of visitors and the total revenue
    total_visitors = (visitors_per_day * 7) + saturday_visitors + sunday_visitors
    total_revenue = total_visitors * ticket_price

    # return the result
    result = total_revenue
    return result

print(solution())
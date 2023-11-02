def solution():
    ticket_price = 3  # The ticket price is $3
    visitors_per_day = 100  # The park is visited by 100 people per day
    visitors_on_sat = 200  # The park is visited by 200 people on Saturday
    visitors_on_sun = 300  # The park is visited by 300 people on Sunday
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total number of visitors for the week
    total_visitors = (visitors_per_day * (days_per_week - 2)) + visitors_on_sat + visitors_on_sun

    # Calculate the total revenue for the week
    total_revenue = total_visitors * ticket_price
    result = total_revenue
    return result

print(solution())
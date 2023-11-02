def solution():
    daily_people = 100
    saturday_people = 200
    sunday_people = 300
    price_per_ticket = 3
    total_people = daily_people + saturday_people + sunday_people
    total_revenue = total_people * price_per_ticket
    return total_revenue

print(solution())
def solution():
    """The zoo has 50 new visitors entering the zoo every hour. The zoo is open for 8 hours in one day. If 80% of the total visitors go to the gorilla exhibit, how many visitors go to the gorilla exhibit in one day?"""
    new_visitors_per_hour = 50
    open_hours_per_day = 8
    total_visitors = new_visitors_per_hour * open_hours_per_day
    gorilla_visitors = 0.8 * total_visitors
    result = gorilla_visitors
    return result

print(solution())
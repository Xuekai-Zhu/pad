def solution():
    """The zoo has 50 new visitors entering the zoo every hour. The zoo is open for 8 hours in one day. If 80% of the total visitors go to the gorilla exhibit, how many visitors go to the gorilla exhibit in one day?"""
    new_visitors_per_hour = 50
    hours_open_per_day = 8
    total_visitors = new_visitors_per_hour * hours_open_per_day
    visitors_to_gorilla_exhibit = total_visitors * 0.8
    result = visitors_to_gorilla_exhibit
    return result

print(solution())
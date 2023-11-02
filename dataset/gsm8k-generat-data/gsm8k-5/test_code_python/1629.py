def solution():
    visitors_per_hour = 50  # 50 new visitors enter the zoo every hour
    open_hours_per_day = 8  # The zoo is open for 8 hours in a day
    total_visitors = visitors_per_hour * open_hours_per_day  # Total number of visitors in one day

    # Calculate the number of visitors going to the gorilla exhibit
    gorilla_visitors = total_visitors * 0.8  # 80% of the visitors go to the gorilla exhibit
    result = gorilla_visitors
    return result

print(solution())
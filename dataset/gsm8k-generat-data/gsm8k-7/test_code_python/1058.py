def solution():
    total_hours = 10
    days = 5
    pages_per_hour = 50
    total_days = 7

    # Calculate the total number of pages Tom reads in 5 days
    total_pages_5_days = total_hours * pages_per_hour * days

    # Calculate the average number of pages Tom reads per day
    avg_pages_per_day = total_pages_5_days / days

    # Calculate the total number of pages Tom reads in 7 days
    total_pages_7_days = avg_pages_per_day * total_days
    result = total_pages_7_days
    return result

print(solution())
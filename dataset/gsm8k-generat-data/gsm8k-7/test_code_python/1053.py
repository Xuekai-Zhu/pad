def solution():
    morning_pages = 5
    evening_pages = 10
    days_in_week = 7

    # Calculate the total number of pages Jane will read in one day
    pages_per_day = morning_pages + evening_pages

    # Calculate the total number of pages Jane will read in one week
    total_pages = pages_per_day * days_in_week
    result = total_pages
    return result

print(solution())
def solution():
    morning_pages = 5  # Jane reads 5 pages in the morning
    evening_pages = 10  # Jane reads 10 pages in the evening
    days_per_week = 7  # There are 7 days in a week
    
    # Calculate the total number of pages Jane will read in a week
    total_pages = (morning_pages + evening_pages) * 2 * days_per_week
    
    result = total_pages
    return result

print(solution())
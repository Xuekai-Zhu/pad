def solution():
    # Calculate the total number of pages read by Steve in a week
    weekly_pages = 100 * 3  # Steve reads 100 pages on Monday, Wednesday and Friday
    # Calculate the number of weeks it takes to read the entire book
    total_weeks = 2100 / weekly_pages  
    result = total_weeks
    return result

print(solution())
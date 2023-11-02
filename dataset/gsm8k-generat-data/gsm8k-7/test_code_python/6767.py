def solution():
    pages_goal = 600
    num_days = 30
    busy_days = 4
    available_day = 23
    available_day_pages = 100

    # Calculate the total number of days Jenna has available to read
    total_available_days = num_days - busy_days + 1

    # Subtract the pages she'll read on the available day
    pages_goal -= available_day_pages

    # Divide the remaining pages by the number of days she has left
    pages_per_day = pages_goal / (total_available_days - 1)

    result = pages_per_day
    return result

print(solution())
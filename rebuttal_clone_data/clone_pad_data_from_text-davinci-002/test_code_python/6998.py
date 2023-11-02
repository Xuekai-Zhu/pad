def solution():
    current_page = 90
    past_page = 60
    pages_left = 210 - current_page
    pages_per_hour = current_page - past_page
    hours_left = pages_left / pages_per_hour
    result = hours_left
    return result

print(solution())
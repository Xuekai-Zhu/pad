def solution():
    words_per_minute = 50
    words_per_page = 400
    pages = 5
    words = words_per_page * pages
    minutes = words / words_per_minute
    hours = minutes / 60
    ounces_per_hour = 15
    total_ounces = hours * ounces_per_hour
    result = total_ounces
    return result

print(solution())
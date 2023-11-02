def solution():
    days_between_letters = 3
    days_in_month = 30
    minutes_per_letter = 20
    minutes_per_page = 10
    extra_minutes_per_page = minutes_per_page * 2
    extra_letter_pages = 80 // extra_minutes_per_page
    normal_letter_pages = ((days_in_month - 1) // days_between_letters) * (minutes_per_letter // minutes_per_page)
    total_pages = extra_letter_pages + normal_letter_pages
    result = total_pages
    return result

print(solution())
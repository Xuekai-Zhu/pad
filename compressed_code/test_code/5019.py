def solution():
    
    total_pages = 60 * 320
    days = 80
    deshaun_pages_per_day = total_pages / days
    second_person_pages = 0.75 * total_pages
    second_person_pages_per_day = second_person_pages / days
    result = second_person_pages_per_day
    return result

print(solution())
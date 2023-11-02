def solution():
    monday_pages = 1
    monday_time = 60
    monday_rate = monday_time / monday_pages
    tuesday_pages = 3
    tuesday_time = 45
    tuesday_rate = tuesday_time / tuesday_pages
    wednesday_pages = 5
    total_pages = monday_pages + tuesday_pages + wednesday_pages
    result = total_pages
    return result

print(solution())
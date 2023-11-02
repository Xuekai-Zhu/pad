def solution():
    
    monday_rate = 30
    monday_time = 60
    monday_pages = monday_time / monday_rate

    tuesday_rate = 15
    tuesday_time = 45
    tuesday_pages = tuesday_time / tuesday_rate

    wednesday_pages = 5

    total_pages = monday_pages + tuesday_pages + wednesday_pages
    result = total_pages
    return result

print(solution())
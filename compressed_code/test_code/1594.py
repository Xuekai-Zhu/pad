def solution():
    
    total_pages = 500
    first_half_pages = total_pages / 2
    second_half_pages = total_pages / 2
    first_half_days = first_half_pages / 10
    second_half_days = second_half_pages / 5
    total_days = first_half_days + second_half_days
    result = total_days
    return result

print(solution())
def solution():
    
    total_loaves = 60
    morning_sales = total_loaves * (2/3)
    remaining_loaves = total_loaves - morning_sales
    afternoon_sales = remaining_loaves * (1/2)
    result = afternoon_sales
    return result

print(solution())
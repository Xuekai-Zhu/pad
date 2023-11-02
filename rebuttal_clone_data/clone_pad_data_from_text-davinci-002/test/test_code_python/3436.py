def solution():
    eggs_per_hour = 2 * 12
    brother_eggs_per_hour = 10
    total_eggs = 170
    hour_total = total_eggs / (eggs_per_hour + brother_eggs_per_hour)
    result = hour_total
    return result

print(solution())
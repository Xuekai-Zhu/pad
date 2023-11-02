def solution():
    lena_hours = 3.5
    lena_minutes = lena_hours * 60
    brother_hours = (lena_minutes + 17) / 60
    brother_minutes = brother_hours * 60
    total_minutes = lena_minutes + brother_minutes
    result = total_minutes
    return result

print(solution())
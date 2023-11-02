def solution():
    
    ivy_length = 40
    strip_per_day = 6
    regrow_per_night = 2
    days = 0
    while ivy_length > 0:
        ivy_length -= strip_per_day
        days += 1
        if ivy_length <= 0:
            break
        ivy_length += regrow_per_night

    result = days
    return result

print(solution())
def solution():
    rabbit_speed = 25
    cat_speed = 20
    lead_time = 15
    rabbit_time = lead_time / rabbit_speed
    cat_time = lead_time / cat_speed
    total_time = rabbit_time + cat_time
    result = total_time
    return result

print(solution())
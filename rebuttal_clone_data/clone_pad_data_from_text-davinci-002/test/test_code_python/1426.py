def solution():
    football_field = 168
    football_field_length = football_field * 4
    time = 8
    rate = football_field_length / time
    minutes = 1
    meters = 500
    total_time = minutes * rate + time
    total_distance = football_field_length + meters
    result = total_distance
    
    return result

print(solution())
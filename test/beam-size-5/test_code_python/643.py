def solution():
    
    soil_rate = 4
    clay_rate = soil_rate / 2
    soil_length = 24
    clay_length = 8
    total_soil_length = soil_length * soil_rate
    total_clay_length = clay_length * clay_rate
    total_time = total_soil_length + total_clay_length
    result = total_time
    return result

print(solution())
def solution():
    # Find the average temperature of Berry for the week
    temp_Sun = 99.1
    temp_Mon = 98.2
    temp_Tue = 98.7
    temp_Wed = 99.3
    temp_Thu = 99.8
    temp_Fri = 99.0
    temp_Sat = 98.9

    avg_temp = (temp_Sun + temp_Mon + temp_Tue + temp_Wed + temp_Thu + temp_Fri + temp_Sat) / 7
    result = avg_temp
    return result

print(solution())
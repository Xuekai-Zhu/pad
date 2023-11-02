def solution():
    
    first_time_rang = 4
    second_time_rang = 3 * first_time_rang
    third_time_rang = second_time_rang / 2
    total_rang = first_time_rang + second_time_rang + third_time_rang
    result = total_rang
    return result

print(solution())
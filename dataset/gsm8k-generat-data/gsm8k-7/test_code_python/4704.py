def solution():
    first_country_duration = 14 # 2 weeks
    second_country_duration = first_country_duration * 2 # double the length of first country
    third_country_duration = second_country_duration # equal to second country
    
    total_duration = first_country_duration + second_country_duration + third_country_duration
    
    result = total_duration
    return result

print(solution())
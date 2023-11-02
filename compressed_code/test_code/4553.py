def solution():
    
    first_hour_rate = 12
    second_hour_rate = 6
    first_hour_tshirts = 60 / first_hour_rate
    second_hour_tshirts = 60 / second_hour_rate
    total_tshirts = first_hour_tshirts + second_hour_tshirts
    result = total_tshirts
    return result

print(solution())
def solution():
    total_tins = 500
    first_day = 50
    second_day = 3 * first_day
    third_day = second_day - 50
    fourth_day = third_day - 50
    fifth_day = fourth_day - 50
    sixth_day = fifth_day - 50
    seventh_day = sixth_day - 50
    result = first_day, second_day, third_day, fourth_day, fifth_day, sixth_day, seventh_day
    
    return result

print(solution())
def solution():
    
    starting_cans = 2000
    first_day_people = 500
    first_day_cans = 500
    restock_1 = 1500
    second_day_people = 1000
    second_day_cans = 2000
    restock_2 = 3000
    total_given_away = first_day_cans + (second_day_people * 2)
    result = total_given_away
    return result

print(solution())
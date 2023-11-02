def solution():
    
    boy_ratio = 5
    girl_ratio = 7
    total_children = 180
    boys = total_children * (boy_ratio / (boy_ratio + girl_ratio))
    money_given = 3900
    money_per_boy = money_given / boys
    result = money_per_boy
    
    return result

print(solution())
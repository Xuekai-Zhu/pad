def solution():
    
    jade_money = 38
    julia_money = jade_money / 2
    total_money = 97
    money_left = total_money - jade_money - julia_money
    aunt_money_per_person = money_left / 2
    result = aunt_money_per_person
    return result

print(solution())
def solution():
    """Jade had $38 and her sister Julia had half as much money she had. On New Year's eve, their aunt gave each of them an equal amount of money so that they had a total of $97. How much did their aunt give each of them?"""
    jade_money = 38
    julia_money = jade_money / 2
    total_money = 97
    money_left = total_money - jade_money - julia_money
    aunt_money_per_person = money_left / 2
    result = aunt_money_per_person
    return result

print(solution())
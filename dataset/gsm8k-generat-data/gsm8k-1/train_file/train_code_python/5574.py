def solution():
    """Jade had $38 and her sister Julia had half as much money she had. On New Year's eve, their aunt gave each of them an equal amount of money so that they had a total of $97. How much did their aunt give each of them?"""
    jade_money = 38
    julia_money = jade_money / 2
    total_money = 97
    money_given_each = (total_money - jade_money - julia_money) / 2
    result = money_given_each
    return result

print(solution())
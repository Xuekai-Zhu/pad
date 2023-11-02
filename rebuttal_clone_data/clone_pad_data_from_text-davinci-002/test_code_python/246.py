def solution():
    """The ratio of boys to girls in a family is 5:7. The total number of children in the family is 180. If the boys are given $3900 to share, how much money does each boy receive?"""
    boy_ratio = 5
    girl_ratio = 7
    total_children = 180
    boys = total_children * (boy_ratio / (boy_ratio + girl_ratio))
    money_given = 3900
    money_per_boy = money_given / boys
    result = money_per_boy
    
    return result

print(solution())
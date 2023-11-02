def solution():
    """Natalia is riding a bicycle for the cycling competition. On Monday she rode 40 kilometers and on Tuesday 50 kilometers. On Wednesday she rode 50% fewer kilometers than the day before. On Thursday she rode as many as the sum of the kilometers from Monday and Wednesday. How many kilometers did Natalie ride in total?"""
    monday_distance = 40
    tuesday_distance = 50
    wednesday_distance = tuesday_distance * 0.5
    thursday_distance = monday_distance + wednesday_distance
    total_distance = monday_distance + tuesday_distance + wednesday_distance + thursday_distance
    result = total_distance
    return result

print(solution())
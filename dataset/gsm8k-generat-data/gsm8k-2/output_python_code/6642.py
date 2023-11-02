def solution():
    """Yuri has been adopting puppies for a month now. The first week he adopted 20 puppies, the second week 2/5 times as many puppies as the first week, the third week twice the number of puppies he adopted in the second week, and the fourth week ten more puppies than he adopted on the first week. How many puppies does Yuri have now?"""
    first_week = 20
    second_week = int(2/5 * first_week)
    third_week = 2 * second_week
    fourth_week = first_week + 10
    total_puppies = first_week + second_week + third_week + fourth_week
    result = total_puppies
    return result

print(solution())
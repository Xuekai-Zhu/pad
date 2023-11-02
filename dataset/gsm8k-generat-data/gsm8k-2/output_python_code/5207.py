def solution():
    """A group of people pays $720 for admission tickets to an amusement park. The price of an adult ticket is $15, and a child ticket is $8. There are 25 more adults than children. How many children are in the group?"""
    total_people = (720 - 8 * x) / 7
    x = 25
    children_num = total_people // 2
    result = children_num
    return result

print(solution())
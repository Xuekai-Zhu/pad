def solution():
    """6 kids in Carolyn's daycare prefer peas, 9 prefer carrots, and 5 prefer corn. What percentage of the children prefer corn?"""
    total_kids = 6 + 9 + 5
    corn_kids = 5
    percent_corn = (corn_kids / total_kids) * 100
    result = percent_corn
    return result

print(solution())
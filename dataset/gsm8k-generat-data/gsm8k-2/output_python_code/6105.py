def solution():
    """There are 8 men at a yoga studio with an average weight of 190 pounds and 6 women with an average weight of 120 pounds. What is the average weight of all 14 men and women?"""
    total_weight = (8 * 190) + (6 * 120)
    total_people = 8 + 6
    average_weight = total_weight / total_people
    result = average_weight
    return result

print(solution())
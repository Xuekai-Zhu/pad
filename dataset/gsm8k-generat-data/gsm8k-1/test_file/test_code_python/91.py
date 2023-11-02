def solution():
    """Out of the 200 Grade 5 students, 2/5 are boys and 2/3 of the girls are in the girl scout. How many girls are not in the girl scout?"""
    total_students = 200
    boys_ratio = 2/5
    girls_ratio = 1 - boys_ratio
    girls_not_in_girl_scout_ratio = 1 - (2/3)
    
    total_girls = total_students * girls_ratio
    girls_not_in_girl_scout = total_girls * girls_not_in_girl_scout_ratio
    result = girls_not_in_girl_scout
    
    return result

print(solution())
def solution():
    """When Nathan is cold, he adds an extra blanket to his bed. Each blanket warms him up by 3 degrees. One night, he was cold enough that he added half of the 14 blankets in his closet on his bed. How many degrees did the blankets warm Nathan up?"""
    blankets = 14
    added_blankets = blankets / 2
    degree_increase_per_blanket = 3
    degrees_warmed = added_blankets * degree_increase_per_blanket
    result = degrees_warmed
    return result

print(solution())
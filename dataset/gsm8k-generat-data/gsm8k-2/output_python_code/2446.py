def solution():
    """When Nathan is cold, he adds an extra blanket to his bed. Each blanket warms him up by 3 degrees. One night, he was cold enough that he added half of the 14 blankets in his closet on his bed. How many degrees did the blankets warm Nathan up?"""
    blankets_in_closet = 14
    added_blankets = blankets_in_closet / 2
    degree_increase_per_blanket = 3
    total_degree_increase = added_blankets * degree_increase_per_blanket
    result = total_degree_increase
    return result

print(solution())
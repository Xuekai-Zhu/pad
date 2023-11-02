def solution():
    """Evie is collecting seashells while at the beach. Each day she collects her favorite 10 shells. At the end of 6 days, she gives 2 shells to her brother. How many shells does she have left?"""
    shells_per_day = 10
    total_shells = shells_per_day * 6
    shells_given = 2
    shells_left = total_shells - shells_given
    result = shells_left
    
    return result

print(solution())
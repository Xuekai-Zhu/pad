def solution():
    """Eddie can bake 3 pies a day. His sister can bake 6 pies while his mother can bake 8 pies a day. How many pies will they be able to bake in 7 days?"""
    eddie_pies_per_day = 3
    sister_pies_per_day = 6
    mother_pies_per_day = 8
    
    total_pies_per_day = eddie_pies_per_day + sister_pies_per_day + mother_pies_per_day
    pies_in_week = total_pies_per_day * 7
    
    result = pies_in_week
    return result

print(solution())
def solution():
    """Eddie can bake 3 pies a day. His sister can bake 6 pies while his mother can bake 8 pies a day. How many pies will they be able to bake in 7 days?"""
    eddie_pies = 3
    sister_pies = 6
    mother_pies = 8
    total_pies_per_day = eddie_pies + sister_pies + mother_pies
    total_days = 7
    total_pies = total_pies_per_day * total_days
    result = total_pies
    return result

print(solution())
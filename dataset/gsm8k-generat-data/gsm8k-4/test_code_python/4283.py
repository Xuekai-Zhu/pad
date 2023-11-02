def solution():
    """Eddie can bake 3 pies a day. His sister can bake 6 pies while his mother can bake 8 pies a day. How many pies will they be able to bake in 7 days?"""
    # Define the number of pies each person can bake per day
    eddie_pies_per_day = 3
    sister_pies_per_day = 6
    mother_pies_per_day = 8

    # Calculate the total number of pies each person can bake in 7 days
    eddie_pies_total = eddie_pies_per_day * 7
    sister_pies_total = sister_pies_per_day * 7
    mother_pies_total = mother_pies_per_day * 7

    # Calculate the total number of pies they can bake together in 7 days
    total_pies = eddie_pies_total + sister_pies_total + mother_pies_total

    # return the result
    result = total_pies
    return result

print(solution())
def solution():
    """Eddie can bake 3 pies a day. His sister can bake 6 pies while his mother can bake 8 pies a day. How many pies will they be able to bake in 7 days?"""
    # Define the number of pies each person can bake per day
    EDDIE_PIES_PER_DAY = 3
    SISTER_PIES_PER_DAY = 6
    MOTHER_PIES_PER_DAY = 8

    # Calculate the total number of pies each person can bake in 7 days
    eddie_pies = EDDIE_PIES_PER_DAY * 7
    sister_pies = SISTER_PIES_PER_DAY * 7
    mother_pies = MOTHER_PIES_PER_DAY * 7

    # Calculate the total number of pies they can bake together in 7 days
    total_pies = eddie_pies + sister_pies + mother_pies

    # Display the total number of pies
    result = total_pies
    return result

print(solution())
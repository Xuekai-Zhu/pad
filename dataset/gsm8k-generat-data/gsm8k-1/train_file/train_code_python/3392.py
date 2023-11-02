def solution():
    """Tomas ate 1.5 pounds of chocolate fudge last week. Katya ate half a pound of peanut butter fudge, while Boris ate 2 pounds of fudge. How many ounces of fudge did the 3 friends eat in total?"""
    tomas_fudge = 1.5
    katya_fudge = 0.5
    boris_fudge = 2
    total_fudge = tomas_fudge + katya_fudge + boris_fudge
    ounces_per_pound = 16
    total_ounces = total_fudge * ounces_per_pound
    result = total_ounces
    return result

print(solution())
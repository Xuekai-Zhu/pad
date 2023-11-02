def solution():
    """Sam is twice as old as Sue. Kendra is 3 times as old as Sam. If Kendra is currently 18, what will be their total age in 3 years?"""
    # Calculate Sam's age
    sam_age = 18/3

    # Calculate Sue's age
    sue_age = sam_age/2

    # Calculate Kendra's age
    kendra_age = 18

    # Calculate the total age in 3 years
    total_age = sam_age + sue_age + kendra_age + 3*3

    # return the result
    result = total_age
    return result

print(solution())
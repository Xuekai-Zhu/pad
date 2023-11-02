def solution():
    maude_age = 8
    emile_ratio = 6
    anne_emile_ratio = 2

    # Calculate Emile's age
    emile_age = maude_age * emile_ratio

    # Calculate Anne's age when Emile is twice as old
    anne_age_emile_twice = emile_age * anne_emile_ratio

    # Calculate Anne's current age
    anne_age = anne_age_emile_twice - (emile_age - maude_age)  # subtract the age difference between Emile and Maude

    result = anne_age
    return result

print(solution())
def solution():
    
    rachel_age = 12
    grandfather_age = 7 * rachel_age
    mother_age = grandfather_age / 2
    father_age = mother_age + 5

    years_to_25 = 25 - rachel_age
    father_age_at_25 = father_age + years_to_25

    result = father_age_at_25
    return result

print(solution())
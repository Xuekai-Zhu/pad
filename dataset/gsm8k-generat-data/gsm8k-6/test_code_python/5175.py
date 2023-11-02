def solution():
    # Find the total age of Kaydence's father, mother, brother, and sister
    father_age = 60
    mother_age = father_age - 2
    brother_age = father_age / 2
    sister_age = 40
    total_family_age = father_age + mother_age + brother_age + sister_age

    # Find Kaydence's age
    kaydence_age = 200 - total_family_age
    result = kaydence_age
    return result

print(solution())
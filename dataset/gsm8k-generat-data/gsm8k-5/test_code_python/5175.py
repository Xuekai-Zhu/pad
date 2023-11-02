def solution():
    father_age = 60
    mother_age = father_age - 2
    brother_age = father_age / 2
    sister_age = 40

    # Find the total age of the rest of the family
    total_others_age = mother_age + brother_age + sister_age

    # Find Kaydence's age by subtracting the total age of the rest of the family from the total family age
    kaydence_age = 200 - total_others_age - father_age
    result = kaydence_age
    return result

print(solution())
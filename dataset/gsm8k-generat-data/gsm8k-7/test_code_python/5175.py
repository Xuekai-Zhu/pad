def solution():
    father_age = 60
    mother_age = father_age - 2
    brother_age = father_age / 2
    sister_age = 40

    # Calculate the total age of everyone except Kaydence
    total_age_without_kaydence = father_age + mother_age + brother_age + sister_age

    # Calculate Kaydence's age using the total age of everyone
    kaydence_age = 200 - total_age_without_kaydence
    result = kaydence_age
    return result

print(solution())
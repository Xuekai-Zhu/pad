def solution():
    total_age = 200
    father_age = 60
    mother_age = father_age - 2
    brother_age = father_age / 2
    sister_age = 40
    kaydence_age = total_age - (father_age + mother_age + brother_age + sister_age)
    result = kaydence_age
    return result

print(solution())
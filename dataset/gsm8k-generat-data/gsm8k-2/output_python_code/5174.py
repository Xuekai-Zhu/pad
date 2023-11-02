def solution():
    """The total age of the people in Kaydence's family is 200. If Kaydence's father is 60 years old, Kaydence's mother 2 years younger than Kaydence's father, Kaydence's brother 1/2 the age of Kaydence's father, and Kaydence's sister 40 years old, how old is Kaydence?"""
    father_age = 60
    mother_age = father_age - 2
    brother_age = father_age / 2
    sister_age = 40
    total_age = father_age + mother_age + brother_age + sister_age + kaydence_age
    kaydence_age = total_age - (father_age + mother_age + brother_age + sister_age)
    result = kaydence_age
    return result

print(solution())
def solution():
    """The total age of the people in Kaydence's family is 200. If Kaydence's father
    is 60 years old, Kaydence's mother 2 years younger than Kaydence's father,
    Kaydence's brother 1/2 the age of Kaydence's father, and Kaydence's sister
    40 years old, how old is Kaydence?"""
    # Define the age of Kaydence's father
    father_age = 60

    # Define the age of Kaydence's mother
    mother_age = father_age - 2

    # Define the age of Kaydence's brother
    brother_age = father_age / 2

    # Define the age of Kaydence's sister
    sister_age = 40

    # Calculate the sum of all family members' ages except Kaydence
    total_age_without_kaydence = father_age + mother_age + brother_age + sister_age

    # Calculate Kaydence's age
    kaydence_age = 200 - total_age_without_kaydence

    # return the result
    result = kaydence_age
    return result

print(solution())
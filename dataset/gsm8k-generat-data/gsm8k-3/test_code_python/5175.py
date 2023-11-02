def solution():
    """The total age of the people in Kaydence's family is 200. If Kaydence's father is 60 years old, Kaydence's mother 2 years younger than Kaydence's father, Kaydence's brother 1/2 the age of Kaydence's father, and Kaydence's sister 40 years old, how old is Kaydence?"""
    # Define Kaydence's father's age
    father_age = 60

    # Define Kaydence's mother's age
    mother_age = father_age - 2

    # Define Kaydence's brother's age
    brother_age = father_age / 2

    # Define Kaydence's sister's age
    sister_age = 40

    # Calculate the total age of Kaydence's family
    total_age = father_age + mother_age + brother_age + sister_age

    # Calculate Kaydence's age
    kaydence_age = total_age - father_age - mother_age - brother_age - sister_age

    # Display Kaydence's age
    result = kaydence_age
    return result

print(solution())
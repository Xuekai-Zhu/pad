def solution():
    """The total for the sum and product of Elvie's age and Arielle's age are 131. If Elvie's age is 10, how old is Arielle?"""
    # Define Elvie's age
    elvies_age = 10

    # Define the total sum and product of their ages
    total = 131
    product = elvies_age * arielles_age

    # Solve for Arielle's age
    # a + b = total - elvies_age
    # ab = product
    # b = product / a
    # a(product / a) = total - elvies_age
    # product = total*a - elvies_age*a
    # a = (total - elvies_age) / (product / elvies_age - elvies_age)

    arielles_age = (total - elvies_age) / (product / elvies_age - elvies_age)

    result = round(arielles_age)
    return result

print(solution())
def solution():
    """The total for the sum and product of Elvie's age and Arielle's age are 131. If Elvie's age is 10, how old is Arielle?"""
    # Define Elvie's age
    elvie_age = 10

    # Calculate the sum and product of Elvie and Arielle's ages
    sum_ages = 131 - elvie_age
    product_ages = sum_ages - elvie_age

    # Solve for Arielle's age using the quadratic formula
    a = 1
    b = -sum_ages
    c = product_ages
    discriminant = b**2 - 4*a*c
    square_root = discriminant**0.5
    arielle_age = (-b + square_root) / (2*a)

    # Display Arielle's age
    result = arielle_age
    return result

print(solution())
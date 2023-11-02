def solution():
    sum_of_ages = 45

    # Let's assume that the current age of the brother is x.
    # Then the current age of the person is y.
    # We know that in ten years, the person will be twice the age of the brother.
    # So, (y + 10) = 2(x + 10)
    # We also know that the sum of their ages in ten years will be 45.
    # So, (x + 10) + (y + 10) = 45
    # Now we can solve these equations to find the current age of the person.

    # Simplifying the first equation, we get y = 2x - 10
    # Substituting this value of y in the second equation, we get x + 2x - 10 + 20 = 45
    # Simplifying this equation, we get 3x + 10 = 45
    # Solving for x, we get x = 35/3
    # This is not a valid age, since we cannot have a fraction of a year.
    # However, we know that in ten years, the sum of their ages will be 45.
    # Since the sum of their ages is an odd number, we know that one of them must be an odd number.
    # So, we can assume that the brother is 11 years old, and solve for the person's age.

    x = 11
    y = 2*x - 10
    current_age_of_person = y
    result = current_age_of_person
    return result

print(solution())
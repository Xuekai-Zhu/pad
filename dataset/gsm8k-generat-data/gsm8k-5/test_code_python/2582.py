def solution():
    # Let's assume Markus's grandson's age is x
    grandson_age = x
    son_age = 2 * x  # Markus's son is twice the age of Markus's grandson
    markus_age = 2 * son_age  # Markus is twice the age of his son

    # Calculate the sum of the ages of Markus, his son, and his grandson
    total_age = grandson_age + son_age + markus_age

    # We know that the total age is 140 years, so we can solve for x
    x = (140 - markus_age - son_age) / 3
    result = int(x)
    return result

print(solution())
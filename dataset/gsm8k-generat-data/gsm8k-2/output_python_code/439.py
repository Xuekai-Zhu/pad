def solution():
    """Cori is 3 years old today. In 5 years, she will be one-third the age of her aunt. How old is her aunt today?"""
    cori_age = 3
    aunt_age = 3 * 3 + 5  # Cori's age in 5 years
    aunt_age *= 3  # Aunt's age in 5 years, which is 1/3 of her current age
    aunt_age -= 5  # Subtract 5 years to get Aunt's current age
    result = aunt_age
    return result

print(solution())
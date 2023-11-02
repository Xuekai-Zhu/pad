def solution():
    mother_age = 80  # Grace's mother is 80 years old
    grandmother_age = 2 * mother_age  # Grace's grandmother is twice the age of her mother
    grace_grandmother_ratio = 3 / 8  # Grace's age is 3/8th the age of her grandmother

    # Calculate Grace's age
    grace_age = (grace_grandmother_ratio * grandmother_age) / (1 + grace_grandmother_ratio)

    result = grace_age
    return result

print(solution())
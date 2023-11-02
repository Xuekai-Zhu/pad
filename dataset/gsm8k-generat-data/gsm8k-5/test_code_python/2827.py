def solution():
    grant_current_age = 25  # Grant is currently 25 years old
    ratio = 2/3  # In five years, Grant will be 2/3 the age of the hospital
    # Let x be the age of the hospital now
    x = (grant_current_age + 5) / ratio - 5  # Solve for x
    result = x
    return result

print(solution())
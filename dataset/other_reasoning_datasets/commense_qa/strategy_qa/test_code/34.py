def solution():
    high_school_age_range = range(14, 20)
    is_digital_native = True
    if min(high_school_age_range) < 1990 and not is_digital_native:
        result = "yes"
    else:
        result = "no"
    return result

# Note: The solution assumes that the yellow pages refer to the physical telephone book that was commonly used before online directories became prevalent.

print(solution())
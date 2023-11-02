def solution():
    initial_count = 180  # Trent initially caught 180 tadpoles
    released_count = initial_count * 0.75  # Trent released 75% of the tadpoles
    kept_count = initial_count - released_count  # Trent kept the remaining tadpoles

    result = kept_count
    return result

print(solution())
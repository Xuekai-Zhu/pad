def solution():
    # Identical twins are always the same gender
    identical_twins_same_gender = True
    # Non-identical twins can be opposite gender or same gender
    non_identical_twins_same_gender = False
    # Check if all twins are the same gender
    if identical_twins_same_gender and not non_identical_twins_same_gender:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
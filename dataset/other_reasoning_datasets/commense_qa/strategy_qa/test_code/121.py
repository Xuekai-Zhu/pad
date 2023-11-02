def solution():
    # Define that tonsils are only found in mammals
    tonsils_only_in_mammals = True
    # Check if fish can get tonsillitis
    if not tonsils_only_in_mammals:
        result = "no"
    else:
        result = "cannot be determined"
    return result

print(solution())
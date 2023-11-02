def solution():
    # Define general albatross accessibility and mollymawk accessibility
    general_accessibility = False  # assume inaccessible
    mollymawk_accessibility = True
    # Check if mollymawks live where general albatrosses cannot
    if not general_accessibility and mollymawk_accessibility:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
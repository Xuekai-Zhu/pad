def solution():
    left_first_wife = False
    # Check if Maria Barbara Bach died suddenly before Johann Sebastian Bach married Anna Magdalena Bach
    if 1720 < 1721:
        left_first_wife = True
    if left_first_wife:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
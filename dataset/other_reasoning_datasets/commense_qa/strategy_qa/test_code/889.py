def solution():
    # Determine if Mercury is a suitable material for a Slip N Slide
    is_Mercury_safe = False
    is_Mercury_a_liquid = True
    if is_Mercury_a_liquid and not is_Mercury_safe:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
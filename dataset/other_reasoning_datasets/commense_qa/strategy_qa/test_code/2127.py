def solution():
    # Check if the person is in a leg cast
    is_in_leg_cast = True
    # Determine if the other foot should be in a sandal
    if is_in_leg_cast:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
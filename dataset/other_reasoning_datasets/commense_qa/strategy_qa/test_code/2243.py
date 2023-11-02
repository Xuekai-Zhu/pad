def solution():
    # Define locations where hippopotamuses can be seen
    us_zoos = True
    uk_zoos = True
    africa = True
    # Check if hippopotamuses can only be seen in Africa
    if not (us_zoos or uk_zoos) and africa:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
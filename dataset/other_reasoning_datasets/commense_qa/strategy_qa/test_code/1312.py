def solution():
    is_natural_born_citizen = False
    birthplace = "Auckland, New Zealand"
    if not is_natural_born_citizen and birthplace != "United States":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())
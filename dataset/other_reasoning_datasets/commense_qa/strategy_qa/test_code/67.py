def solution():
    age_difference = Snoopy_age - Taylor_age
    if age_difference >= 10:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
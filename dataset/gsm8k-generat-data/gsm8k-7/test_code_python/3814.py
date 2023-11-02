def solution():
    ladybugs_on_monday = 8
    ladybugs_on_tuesday = 5
    dots_per_ladybug = 6

    # Calculate the total number of ladybugs caught
    total_ladybugs = ladybugs_on_monday + ladybugs_on_tuesday

    # Calculate the total number of dots on all the ladybugs
    total_dots = total_ladybugs * dots_per_ladybug
    result = total_dots
    return result

print(solution())
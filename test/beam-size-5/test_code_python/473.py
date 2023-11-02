def solution():
    total_kids = 32  # There are 32 kids in Gina's class
    allergic_to_dairy = 9  # 9 kids are allergic to dairy
    allergic_to_peanuts = 6  # 6 kids are allergic to peanuts
    allergic_to_both = 3  # 3 kids are allergic to both

    # Calculate the number of allergic to any
    allergic_to_any = total_kids - allergic_to_dairy - allergic_to_peanuts - allergic_to_both
    result = allergic_to_any
    return result

print(solution())
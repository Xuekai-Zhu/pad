def solution():
    # Calculate the number of apples used for the kids' teachers
    apples_to_teachers = 2 * 2 * 3  # each kid takes 3 apples to 2 teachers

    # Calculate the number of apples used for the pies
    apples_for_pies = 10 * 2  # Jill bakes 2 pies using 10 apples each

    # Calculate the total number of apples used
    total_apples_used = apples_to_teachers + apples_for_pies

    # Calculate the number of apples left
    apples_left = 50 - total_apples_used
    result = apples_left
    return result

print(solution())
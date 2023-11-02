def solution():
    # Calculate the total number of apples picked
    total_apples_picked = 50

    # Calculate the number of apples used to give to the teachers
    apples_for_teachers = 2 * 2 * 3

    # Calculate the number of apples used for the pies
    apples_for_pies = 2 * 10

    # Calculate the total number of apples used
    total_apples_used = apples_for_teachers + apples_for_pies

    # Calculate the number of apples left
    apples_left = total_apples_picked - total_apples_used
    result = apples_left
    return result

print(solution())
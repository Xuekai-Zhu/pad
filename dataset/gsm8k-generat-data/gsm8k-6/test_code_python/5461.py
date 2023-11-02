def solution():
    # Calculate the number of clovers with 3 petals
    clovers_with_3_petals = 0.75 * 200

    # Calculate the number of clovers with 2 petals
    clovers_with_2_petals = 0.24 * 200

    # Calculate the number of clovers with 4 petals
    clovers_with_4_petals = 0.01 * 200

    # Calculate the total number of cloverleaves picked
    total_cloverleaves = 3 * clovers_with_3_petals + 2 * clovers_with_2_petals + 4 * clovers_with_4_petals

    # Calculate the amount earned by June
    cents_earned = total_cloverleaves

    result = cents_earned
    return result

print(solution())
def solution():
    # The number of golden apples charged by Hephaestus for the first six months
    apples_first_half = 3

    # The number of golden apples charged by Hephaestus for the second six months
    apples_second_half = 2 * apples_first_half

    # The total number of golden apples charged by Hephaestus for the entire year of chariot wheels
    total_apples = apples_first_half + apples_second_half
    result = total_apples
    return result

print(solution())
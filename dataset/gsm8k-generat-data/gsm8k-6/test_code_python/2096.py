def solution():
    # Use the given information to determine how many cans of corn Beth bought
    cans_of_peas = 35
    cans_of_peas_formula = 2 * cans_of_corn + 15
    cans_of_corn = (cans_of_peas_formula - 15) / 2
    result = cans_of_corn
    return result

print(solution())
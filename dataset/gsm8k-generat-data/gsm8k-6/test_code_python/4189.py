def solution():
    # Find Mr. Bernard's age in eight years
    Bernard_age_in_8_years = 3 * 20

    # Find Mr. Bernard's current age
    Bernard_current_age = Bernard_age_in_8_years - 8

    # Find the average age of Mr. Bernard and Luke
    average_age = (Bernard_current_age + 20) / 2

    # Find 10 years less than their average age
    ten_years_less = average_age - 10

    result = ten_years_less
    return result

print(solution())
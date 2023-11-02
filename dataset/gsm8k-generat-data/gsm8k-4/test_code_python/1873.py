def solution():
    """The sum of the ages of Jeremy, Sebastian and Sophia in three years is 150. Currently, Sebastian is 4 years older than Jeremy. If Jeremy's age is 40, calculate Sophia's age three years from now?"""
    # Define Jeremy's current age
    jeremy_age = 40

    # Define Sebastian's current age
    sebastian_age = jeremy_age + 4

    # Calculate the sum of their ages in three years
    total_age_in_three_years = 150

    # Calculate the sum of their current ages
    total_current_age = (jeremy_age + sebastian_age + s) - (3 * 3)

    # Calculate Sophia's current age
    sophia_age = total_current_age - (jeremy_age + sebastian_age)

    # Calculate Sophia's age in three years
    sophia_age_in_three_years = sophia_age + 3

    # return the result
    result = sophia_age_in_three_years
    return result

print(solution())
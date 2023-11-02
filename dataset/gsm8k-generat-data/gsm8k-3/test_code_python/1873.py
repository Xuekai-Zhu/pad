def solution():
    """The sum of the ages of Jeremy, Sebastian and Sophia in three years is 150.
    Currently, Sebastian is 4 years older than Jeremy. If Jeremy's age is 40, 
    calculate Sophia's age three years from now?"""
    # Calculate Sebastian's current age
    sebastian_age = 40 + 4

    # Calculate the sum of their ages in three years
    sum_in_three_years = 150 - 3 * 3

    # Calculate the sum of Jeremy and Sebastian's ages in three years
    jeremy_sebastian_sum = sebastian_age + 40 + 2 * 3

    # Calculate Sophia's age in three years
    sophia_age = sum_in_three_years - jeremy_sebastian_sum

    # Calculate Sophia's age currently
    sophia_current_age = sophia_age - 3

    # Display Sophia's age in three years
    result = sophia_current_age + 3
    return result

print(solution())
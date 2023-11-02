def solution():
    """Five years ago, the sum of Sebastian's age and his sister's age was 3/4 of their father's age. How old is their father today if Sebastian is 40 years old and 10 years older than his sister?"""
    # Define Sebastian's age
    sebastian_age = 40

    # Define Sebastian's sister's age
    sister_age = sebastian_age - 10

    # Calculate the sum of their ages 5 years ago
    sum_ages_5_years_ago = (sebastian_age - 5) + (sister_age - 5)

    # Calculate their father's age 5 years ago
    father_age_5_years_ago = 4/3 * sum_ages_5_years_ago

    # Calculate their father's current age
    father_age = father_age_5_years_ago + 5 * 2

    # Display their father's current age
    result = father_age
    return result

print(solution())
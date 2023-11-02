def solution():
    """Josiah is three times as old as Hans. Hans is 15 years old now. In three years, what is the sum of the ages of Josiah and Hans?"""
    # Define Hans' current age
    hans_age = 15

    # Calculate Josiah's current age
    josiah_age = 3 * hans_age

    # Calculate the sum of their ages in three years
    hans_age_in_3_years = hans_age + 3
    josiah_age_in_3_years = josiah_age + 3
    sum_of_ages_in_3_years = hans_age_in_3_years + josiah_age_in_3_years

    # Display the sum of their ages in three years
    result = sum_of_ages_in_3_years
    return result

print(solution())
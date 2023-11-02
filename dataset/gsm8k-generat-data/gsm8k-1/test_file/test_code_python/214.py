def solution():
    """Adrian's age is three times the age of Harriet, and Harriet is half the age of Zack. Calculate the average age of the three in three years if Harriet is 21 years old now."""
    harriet_age = 21
    zack_age = 2 * harriet_age
    adrian_age = 3 * harriet_age
    harriet_age_in_three_years = harriet_age + 3
    zack_age_in_three_years = zack_age + 3
    adrian_age_in_three_years = adrian_age + 3
    total_age_in_three_years = harriet_age_in_three_years + zack_age_in_three_years + adrian_age_in_three_years
    average_age_in_three_years = total_age_in_three_years / 3
    result = average_age_in_three_years
    return result

print(solution())
def solution():
    hans_age_now = 15
    josiah_age_now = hans_age_now * 3

    # Calculate the ages of Hans and Josiah in three years
    hans_age_in_three_years = hans_age_now + 3
    josiah_age_in_three_years = josiah_age_now + 3

    # Calculate the sum of their ages in three years
    sum_of_ages_in_three_years = hans_age_in_three_years + josiah_age_in_three_years
    result = sum_of_ages_in_three_years
    return result

print(solution())
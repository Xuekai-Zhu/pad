def solution():
    # Let's use variables to represent Josh's age when they got married and the current year
    josh_age_married = 22
    current_year = 2021

    # We know that they've been married for 30 years, so we can calculate the year they got married
    year_married = current_year - 30

    # We know Josh's age when they got married and the year they got married, so we can calculate Josh's birth year
    josh_birth_year = year_married - josh_age_married

    # We also know that their combined age today is 5 times Josh's age when they got married
    combined_age_today = 5 * josh_age_married

    # Let's use a variable to represent Anna's age when they got married
    anna_age_married = combined_age_today - josh_age_married

    # Now we can calculate Anna's birth year
    anna_birth_year = year_married - anna_age_married

    # Finally, we can calculate Anna's age when they got married
    anna_age_when_married = josh_age_married - (anna_birth_year - josh_birth_year)

    result = anna_age_when_married
    return result

print(solution())
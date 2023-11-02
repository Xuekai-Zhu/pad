def solution():
    """Josh and Anna were both born on August 17th, but in different years. To consolidate celebrations they also got married on August 17 when Josh turned 22. If today they're celebrating 30 years of marriage and their combined age is exactly 5 times what Josh's age was when they married, how old was Anna when they got married?"""
    # Define Josh's age when they got married
    josh_age_married = 22

    # Define the number of years they've been married
    years_married = 30

    # Calculate Josh's current age
    josh_age_current = josh_age_married + years_married

    # Calculate the combined age of Josh and Anna when they got married
    combined_age_married = josh_age_married * 2

    # Calculate the current combined age of Josh and Anna
    combined_age_current = josh_age_current + josh_age_married

    # Calculate Anna's age when they got married
    anna_age_married = combined_age_married - josh_age_married

    result = anna_age_married
    return result

print(solution())
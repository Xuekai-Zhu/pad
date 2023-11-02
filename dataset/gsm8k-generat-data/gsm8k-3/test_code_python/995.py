def solution():
    """Josh and Anna were both born on August 17th, but in different years. To consolidate celebrations they also got married on August 17 when Josh turned 22. If today they're celebrating 30 years of marriage and their combined age is exactly 5 times what Josh's age was when they married, how old was Anna when they got married?"""
    # Calculate how old Josh is now
    josh_age_now = 22 + 30

    # Calculate what Josh's age was when they got married
    josh_age_married = 22

    # Calculate the combined age of Josh and Anna now
    combined_age_now = josh_age_now * 2

    # Calculate what the combined age was when they got married
    combined_age_married = josh_age_married * 5

    # Calculate how old Anna was when they got married
    anna_age_married = combined_age_married - josh_age_married

    # Display Anna's age when they got married
    result = anna_age_married
    return result

print(solution())
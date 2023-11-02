def solution():
    """Josh and Anna were both born on August 17th, but in different years. To consolidate celebrations they also got married on August 17 when Josh turned 22. If today they're celebrating 30 years of marriage and their combined age is exactly 5 times what Josh's age was when they married, how old was Anna when they got married?"""
    josh_age_when_married = 22
    current_marriage_years = 30
    current_josh_age = josh_age_when_married + current_marriage_years
    current_combined_age = current_josh_age * 5
    anna_age_when_married = current_combined_age - josh_age_when_married
    result = anna_age_when_married
    return result

print(solution())
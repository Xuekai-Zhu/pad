def solution():
    """Josh and Anna were both born on August 17th, but in different years. To consolidate celebrations they also got married on August 17 when Josh turned 22. If today they're celebrating 30 years of marriage and their combined age is exactly 5 times what Josh's age was when they married, how old was Anna when they got married?"""
    josh_age_when_married = 22
    combined_age_at_marriage = 5 * josh_age_when_married
    combined_age_today = combined_age_at_marriage + 30
    anna_age_today = combined_age_today - josh_age_when_married
    anna_age_at_marriage = anna_age_today - 30
    result = anna_age_at_marriage
    return result

print(solution())
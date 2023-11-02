def solution():
    josh_marriage_age = 22  # Josh got married at the age of 22
    combined_age_at_marriage = josh_marriage_age * 2  # Combined age of Josh and Anna when they got married
    combined_age_today = 5 * josh_marriage_age  # Combined age of Josh and Anna today

    # Calculate Anna's age when they got married
    anna_marriage_age = combined_age_at_marriage - josh_marriage_age
    result = anna_marriage_age
    return result

print(solution())
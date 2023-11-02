def solution():
    # Define the facts about Jonas Salk and the treatment of heart attacks
    developed_polio_vaccine = True
    died_of_heart_attack = True
    commonly_treated_with_beta_blockers = True
    # Check if the polio medicine saved Salk's life
    if developed_polio_vaccine and not died_of_heart_attack and not commonly_treated_with_beta_blockers:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
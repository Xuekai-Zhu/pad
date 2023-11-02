def solution():
    grandmother_age = 75  # Cara's grandmother is 75 years old
    mom_age = grandmother_age - 15  # Cara's mom is 15 years younger than her grandmother
    cara_mom_age_diff = 20  # Cara is 20 years younger than her mom

    # Calculate Cara's age
    cara_age = mom_age - cara_mom_age_diff
    result = cara_age
    return result

print(solution())
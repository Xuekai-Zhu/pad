def solution():
    piggy_bank_total = 43  # Jack currently has $43 in his piggy bank
    allowance_weekly = 10  # Jack gets $10 allowance every week
    allowance_half = allowance_weekly / 2  # Jack puts half of his allowance into his piggy bank every week
    weeks = 8  # Jack wants to know how much he will have in his piggy bank after 8 weeks

    # Calculate the total amount of money Jack puts into his piggy bank over 8 weeks
    total_saved = allowance_half * weeks

    # Add the total amount Jack saved to the initial amount in his piggy bank
    final_amount = piggy_bank_total + total_saved
    result = final_amount
    return result

print(solution())
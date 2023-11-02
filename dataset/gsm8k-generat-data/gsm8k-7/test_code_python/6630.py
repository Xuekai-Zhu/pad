def solution():
    total_donation = 240

    # Calculate the amount for the community pantry project
    pantry_amt = total_donation / 3

    # Calculate the amount for the local crisis fund
    crisis_amt = total_donation / 2

    # Calculate the remaining amount
    remaining_amt = total_donation - pantry_amt - crisis_amt

    # Calculate the amount for livelihood project funds
    livelihood_amt = remaining_amt / 4

    # Calculate the amount for contingency funds
    contingency_amt = remaining_amt - livelihood_amt

    result = contingency_amt
    return result

print(solution())
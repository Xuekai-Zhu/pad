def solution():
    """If Lyn donates $240 to a private organization each year where 1/3 of it goes to the community pantry project, 1/2 goes to the local crisis fund, 1/4 of the remaining goes to livelihood project funds, and the rest is for contingency funds. How much goes to contingency fund?"""
    # Define the total donation amount
    total_donation = 240

    # Calculate the amount that goes to the community pantry project
    pantry_amount = total_donation / 3

    # Calculate the amount that goes to the local crisis fund
    crisis_amount = total_donation / 2

    # Calculate the remaining amount for livelihood project funds and contingency funds
    remaining_amount = total_donation - pantry_amount - crisis_amount
    livelihood_amount = remaining_amount / 4
    contingency_amount = remaining_amount - livelihood_amount

    # Display the amount for contingency funds
    result = contingency_amount
    return result

print(solution())
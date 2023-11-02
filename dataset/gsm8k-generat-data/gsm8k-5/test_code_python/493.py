def solution():
    attendees = 50  # There were 50 people at the party
    contribution_per_person = 100  # Each attendee had to pay $100
    total_contribution = attendees * contribution_per_person  # Calculate the total contributions

    total_expenses = total_contribution - 500  # The total expenses were $500 less than the total contributions

    # Calculate the amount of money used to pay for party expenses
    party_expenses = total_contribution - total_expenses
    result = party_expenses
    return result

print(solution())
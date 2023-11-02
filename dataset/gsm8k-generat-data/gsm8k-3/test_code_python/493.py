def solution():
    """Hally and her friends organized a high school reunion. To cover the cost of a late-night party that they planned for at the reunion, each attendee had to pay $100. After the party, Hally and her friends realized that the total expenses were $500 less than the total contributions. If there were 50 people at the party, how much money was used to pay for the party expenses?"""
    # Define the cost per attendee
    COST_PER_ATTENDEE = 100

    # Define the number of attendees
    num_attendees = 50

    # Calculate the total contributions
    total_contributions = COST_PER_ATTENDEE * num_attendees

    # Calculate the total expenses
    total_expenses = total_contributions - 500

    # Display the total amount used to pay for party expenses
    result = total_expenses
    return result

print(solution())
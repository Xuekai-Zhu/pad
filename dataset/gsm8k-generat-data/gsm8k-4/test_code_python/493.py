def solution():
    """Hally and her friends organized a high school reunion. To cover the cost of a late-night party that they planned for at the reunion, each attendee had to pay $100. After the party, Hally and her friends realized that the total expenses were $500 less than the total contributions. If there were 50 people at the party, how much money was used to pay for the party expenses?"""
    # Define the number of attendees and the cost per person
    attendees = 50
    cost_per_person = 100

    # Calculate the total contributions from the attendees
    total_contributions = attendees * cost_per_person

    # Calculate the total expenses
    total_expenses = total_contributions - 500

    # return the result
    result = total_expenses
    return result

print(solution())
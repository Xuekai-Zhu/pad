def solution():
    """Hally and her friends organized a high school reunion. To cover the cost of a late-night party that they planned for at the reunion, each attendee had to pay $100. After the party, Hally and her friends realized that the total expenses were $500 less than the total contributions. If there were 50 people at the party, how much money was used to pay for the party expenses?"""
    attendees = 50
    cost_per_person = 100
    total_cost = attendees * cost_per_person
    expenses = total_cost - 500
    result = expenses
    return result

print(solution())
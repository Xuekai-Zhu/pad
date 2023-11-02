def solution():
    """Tom attends a party that collects $2000.  Half the school attended and the school had 400 people.  How much would they have made if 300 people attended?"""
    # Calculate the amount collected per person at the party
    amount_per_person = 2000 / (400 / 2)

    # Calculate the amount that would have been collected if 300 people attended
    amount_collected = amount_per_person * 300

    result = amount_collected
    return result

print(solution())
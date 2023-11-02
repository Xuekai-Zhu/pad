def solution():
    """Tom attends a party that collects $2000. Half the school attended and the school had 400 people. How much would they have made if 300 people attended?"""
    total_attendees = 400
    half_attended = total_attendees / 2
    collected_amount = 2000
    collected_amount_per_person = collected_amount / half_attended
    new_attendees = 300
    new_collected_amount = collected_amount_per_person * (half_attended + new_attendees)
    result = new_collected_amount
    return result

print(solution())
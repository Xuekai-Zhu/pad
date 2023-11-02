def solution():
    """Heather is going to sew 150 aprons that are to be used for a kiddie crew program. She already was able to sew  13 aprons, and today, she sewed three times as many aprons. How many aprons should she sew tomorrow if she wants to sew half of the remaining number of aprons needed?"""
    # Define the total number of aprons needed
    total_aprons = 150

    # Calculate the number of aprons already sewn by Heather
    aprons_sewn = 13

    # Calculate the number of aprons sewn today
    aprons_sewn_today = 3 * aprons_sewn

    # Calculate the number of aprons still needed
    aprons_remaining = total_aprons - aprons_sewn - aprons_sewn_today

    # Calculate the number of aprons Heather needs to sew tomorrow to fulfill half of the remaining number of aprons
    aprons_needed_tomorrow = aprons_remaining / 2

    result = aprons_needed_tomorrow
    return result

print(solution())
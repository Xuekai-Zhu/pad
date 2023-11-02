def solution():
    """Heather is going to sew 150 aprons that are to be used for a kiddie crew program. She already was able to sew  13 aprons, and today, she sewed three times as many aprons. How many aprons should she sew tomorrow if she wants to sew half of the remaining number of aprons needed?"""
    # Define the total number of aprons needed
    total_aprons = 150

    # Define the number of aprons already sewn
    aprons_sewn = 13

    # Calculate the number of aprons sewn today
    aprons_today = 3 * aprons_sewn

    # Calculate the remaining number of aprons needed
    remaining_aprons = total_aprons - aprons_sewn - aprons_today

    # Calculate the number of aprons Heather should sew tomorrow
    aprons_tomorrow = remaining_aprons / 2

    # Display the number of aprons Heather should sew tomorrow
    result = aprons_tomorrow
    return result

print(solution())
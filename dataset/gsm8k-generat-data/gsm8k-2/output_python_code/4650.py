def solution():
    """Heather is going to sew 150 aprons that are to be used for a kiddie crew program. She already was able to sew 13 aprons, and today, she sewed three times as many aprons. How many aprons should she sew tomorrow if she wants to sew half of the remaining number of aprons needed?"""
    remaining_aprons = 150 - 13 - (3*13)
    aprons_to_sew = remaining_aprons / 2
    aprons_sewn_today = (3*13)
    aprons_to_sew_tomorrow = aprons_to_sew - aprons_sewn_today
    result = aprons_to_sew_tomorrow
    return result

print(solution())
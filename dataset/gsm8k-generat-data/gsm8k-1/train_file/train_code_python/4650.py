def solution():
    """Heather is going to sew 150 aprons that are to be used for a kiddie crew program. She already sewed 13 aprons, and today she sewed three times as many aprons. How many aprons should she sew tomorrow if she wants to sew half of the remaining number of aprons needed?"""
    total_aprons = 150
    aprons_sewn = 13
    today_aprons = 3 * aprons_sewn
    remaining_aprons = total_aprons - aprons_sewn - today_aprons
    aprons_to_sew_tomorrow = remaining_aprons / 2
    result = aprons_to_sew_tomorrow
    return result

print(solution())
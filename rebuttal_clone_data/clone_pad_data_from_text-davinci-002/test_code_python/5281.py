def solution():
    husband_contribution = 335
    wife_contribution = 225
    weeks_saved = 6 * 4
    couple_savings = (husband_contribution + wife_contribution) * weeks_saved
    child_savings = couple_savings / 4
    result = child_savings
    return result

print(solution())
def solution():
    
    husband_contribution = 335
    wife_contribution = 225
    num_of_weeks = 4 * 6
    total_savings = (husband_contribution + wife_contribution) * num_of_weeks
    amount_per_child = total_savings / 2 / 4
    result = amount_per_child

    return result

print(solution())
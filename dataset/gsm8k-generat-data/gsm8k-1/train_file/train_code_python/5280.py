def solution():
    """A couple opened a savings account. The husband gives $335 every week while the wife gives $225 every week. After 6 months of saving (assume 4 weeks in each month), they decided to divide half of the couple's savings into their four children's savings accounts. How much does each child receive?"""
    husband_contribution = 335
    wife_contribution = 225
    num_of_weeks = 4 * 6
    total_savings = (husband_contribution + wife_contribution) * num_of_weeks
    amount_per_child = total_savings / 2 / 4
    result = amount_per_child

    return result

print(solution())
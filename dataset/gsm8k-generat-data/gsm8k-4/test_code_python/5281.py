def solution():
    """A couple opened a savings account. The husband gives $335 every week while the wife gives $225 every week. After 6 months of saving (assume 4 weeks in each month), they decided to divide half of the couple's savings into their four children's savings accounts. How much does each child receive?"""
    # Define the savings of the couple
    husband_savings = 335 * 4 * 26 / 2
    wife_savings = 225 * 4 * 26 / 2
    total_savings = husband_savings + wife_savings

    # Divide the savings equally among the 4 children
    children_share = total_savings / 2 / 4

    # Return the result
    result = children_share
    return result

print(solution())
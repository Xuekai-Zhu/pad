def solution():
    """A couple opened a savings account. The husband gives $335 every week while the wife gives $225 every week.
    After 6 months of saving (assume 4 weeks in each month), they decided to divide half of the couple's savings into their four children's savings accounts.
    How much does each child receive?"""
    # Define the amount of money the husband and wife save each week
    husband_savings = 335
    wife_savings = 225

    # Calculate the total savings after 6 months
    total_savings = (husband_savings + wife_savings) * 4 * 6

    # Determine the amount of savings to be divided among the children
    children_savings = total_savings / 2

    # Determine how much each child will receive
    amount_per_child = children_savings / 4

    # Display the amount each child will receive
    result = amount_per_child
    return result

print(solution())
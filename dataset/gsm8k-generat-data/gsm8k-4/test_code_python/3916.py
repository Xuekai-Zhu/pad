def solution():
    """Thomas has been saving $40 in the bank every month for six years. His friend Joseph has been saving 2/5 times less money per month. How much money are they having in their savings account altogether?"""
    # Define the savings for Thomas and Joseph
    thomas_savings = 40 * 12 * 6
    joseph_savings = (3/5) * 40 * 12 * 6

    # Calculate the total savings
    total_savings = thomas_savings + joseph_savings

    # return the result
    result = total_savings
    return result

print(solution())
def solution():
    """Thomas has been saving $40 in the bank every month for six years. His friend Joseph has been saving 2/5 times less money per month. How much money are they having in their savings account altogether?"""
    thomas_savings = 40 * 12 * 6
    joseph_savings = (3/5) * 40 * 12 * 6
    total_savings = thomas_savings + joseph_savings
    result = total_savings
    return result

print(solution())
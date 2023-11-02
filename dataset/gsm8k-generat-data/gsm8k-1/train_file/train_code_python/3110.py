def solution():
    """John decides to get a new apartment with a roommate. His former rent was $2 per square foot for a 750 square foot apartment. His new apartment cost $2800 per month, which he splits evenly with the roommate. How much money does he save a year?"""
    former_rent = 2 * 750
    new_rent = 2800 * 12 / 2
    savings = former_rent - new_rent
    result = savings
    return result

print(solution())
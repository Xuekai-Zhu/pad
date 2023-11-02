def solution():
    initial_funding = 100000  # John's initial funding of $100,000 for the first 5 months
    additional_funding = initial_funding * 1.5  # John's research takes 50% more funding per month after the first 5 months
    total_funding = initial_funding + (10 * additional_funding)  # John's total funding for the first 5 months
    research_cost = total_funding * 100  # John's research costs $100,000 for the first 5 months
    result = research_cost
    return result

print(solution())
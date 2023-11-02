def solution():
    """Amber goes to the store and buys 10 rolls of toilet paper, 7 rolls of paper towels, and 3 boxes of tissues. One roll of toilet paper costs $1.50. One roll of paper towels costs $2. If the total cost of all the items is $35, how much does one box of tissues cost?"""
    toilet_paper_cost = 1.5
    paper_towels_cost = 2
    tissues_cost = (35 - (10 * toilet_paper_cost) - (7 * paper_towels_cost)) / 3
    result = tissues_cost
    return result

print(solution())
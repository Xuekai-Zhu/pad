def solution():
    """Amber goes to the store and buys 10 rolls of toilet paper, 7 rolls of paper towels, and 3 boxes of tissues. One roll of toilet paper costs $1.50. One roll of paper towels costs $2. If the total cost of all the items is $35, how much does one box of tissues cost?"""
    toilet_paper_cost = 1.5
    paper_towel_cost = 2
    num_toilet_paper = 10
    num_paper_towels = 7
    num_tissues = 3
    total_cost = 35
    tissues_cost = (total_cost - (toilet_paper_cost*num_toilet_paper) - (paper_towel_cost*num_paper_towels)) / num_tissues
    result = tissues_cost
    return result

print(solution())
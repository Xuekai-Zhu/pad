def solution():
    """Amber goes to the store and buys 10 rolls of toilet paper, 7 rolls of paper towels, and 3 boxes of tissues. One roll of toilet paper costs $1.50. One roll of paper towels costs $2. If the total cost of all the items is $35, how much does one box of tissues cost?"""
    # Define the cost of each item
    TOILET_PAPER_COST = 1.5
    PAPER_TOWELS_COST = 2

    # Define the number of each item purchased
    toilet_paper = 10
    paper_towels = 7
    tissues = 3

    # Calculate the total cost of the toilet paper
    toilet_paper_cost = toilet_paper * TOILET_PAPER_COST

    # Calculate the total cost of the paper towels
    paper_towels_cost = paper_towels * PAPER_TOWELS_COST

    # Calculate the cost of the tissues
    tissues_cost = 35 - toilet_paper_cost - paper_towels_cost

    # Calculate the cost of one box of tissues
    cost_per_box = tissues_cost / tissues

    # Display the cost of one box of tissues
    result = cost_per_box
    return result

print(solution())
def solution():
    """Amber goes to the store and buys 10 rolls of toilet paper, 7 rolls of paper towels, and 3 boxes of tissues. 
    One roll of toilet paper costs $1.50. One roll of paper towels costs $2. If the total cost of all the items is $35, 
    how much does one box of tissues cost?"""
    # Define the prices of toilet paper and paper towels
    toilet_paper_price = 1.5
    paper_towels_price = 2

    # Define the quantities of toilet paper, paper towels, and tissues
    toilet_paper_quantity = 10
    paper_towels_quantity = 7
    tissues_quantity = 3

    # Calculate the total cost of toilet paper and paper towels
    toilet_paper_cost = toilet_paper_quantity * toilet_paper_price
    paper_towels_cost = paper_towels_quantity * paper_towels_price

    # Calculate the cost of the tissues
    tissues_cost = 35 - toilet_paper_cost - paper_towels_cost

    # Calculate the cost of one box of tissues
    box_of_tissues_cost = tissues_cost / tissues_quantity

    # Return the result
    result = box_of_tissues_cost
    return result

print(solution())
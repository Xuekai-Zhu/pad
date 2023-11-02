def solution():
    pages_per_copy = 25  # Jenny's essay has 25 pages
    num_copies = 7  # Jenny wants to print 7 copies of her essay
    cost_per_page = 0.10  # It costs $0.10 to print one page
    num_pens = 7  # Jenny wants to buy 7 pens that each cost $1.50
    pen_cost = 1.50  # Each pen costs $1.50
    total_paper_cost = pages_per_copy * num_copies * cost_per_page  # Total cost of printing the essay
    total_pen_cost = num_pens * pen_cost  # Total cost of buying pens
    total_cost = total_paper_cost + total_pen_cost  # Total cost of everything
    amount_paid = 40.00  # Jenny pays with two $20 bills
    change = amount_paid - total_cost  # Calculate the change

    result = change
    return result

print(solution())
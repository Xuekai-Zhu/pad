def solution():
    cost_per_page = 0.1
    num_copies = 7
    num_pages = 25
    cost_per_pen = 1.5
    num_pens = 7
    cash_paid = 40  # 2 twenty dollar bills

    # Calculate the total cost of printing the essay
    printing_cost = cost_per_page * num_copies * num_pages

    # Calculate the total cost of buying the pens
    pen_cost = cost_per_pen * num_pens

    # Calculate the total cost of everything
    total_cost = printing_cost + pen_cost

    # Calculate the change that Jenny should get
    change = cash_paid - total_cost
    result = change
    return result

print(solution())
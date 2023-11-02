def solution():
    num_pens = 4
    pen_price = 1.5

    num_notebooks = 2
    notebook_price = 4

    bond_paper_price = 20

    # Calculate the total cost of all pens
    total_pen_cost = num_pens * pen_price

    # Calculate the total cost of all notebooks
    total_notebook_cost = num_notebooks * notebook_price

    # Calculate the total cost of all bond paper
    total_paper_cost = bond_paper_price

    # Calculate the total cost of all supplies
    total_cost = total_pen_cost + total_notebook_cost + total_paper_cost
    result = total_cost
    return result

print(solution())
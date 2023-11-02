def solution():
    notebook_price = 1.5
    pen_price = 0.25
    calculator_price = 12
    geometry_set_price = 10

    num_notebooks = 5
    num_pens = 2
    num_calculators = 1
    num_geometry_sets = 1

    discount = 0.1  # 10% discount

    # Calculate the total cost of all items
    total_notebook_cost = num_notebooks * notebook_price
    total_pen_cost = num_pens * pen_price
    total_calculator_cost = num_calculators * calculator_price
    total_geometry_cost = num_geometry_sets * geometry_set_price

    # Calculate the total cost before discount
    total_cost_before_discount = total_notebook_cost + total_pen_cost + total_calculator_cost + total_geometry_cost

    # Calculate the discount
    discount_amount = total_cost_before_discount * discount

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before

print(solution())
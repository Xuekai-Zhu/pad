def solution():
    num_boxes = 12
    pens_per_box = 30
    box_cost = 10

    num_packages = 5
    pens_per_package = 6
    package_price = 3

    pens_per_set = 3
    set_price = 2

    # Calculate the total cost of buying all the boxes of highlighters
    total_cost = num_boxes * box_cost

    # Calculate the total number of highlighter pens Sam has
    total_pens = num_boxes * pens_per_box

    # Calculate the total number of pens he sells in packages
    total_package_pens = num_packages * pens_per_package

    # Calculate the total number of pens he sells individually
    total_single_pens = total_pens - total_package_pens

    # Calculate the total revenue from selling highlighters in packages
    total_package_revenue = num_packages * package_price

    # Calculate the total revenue from selling individual highlighters
    total_single_revenue = (total_single_pens / pens_per_set) * set_price

    # Calculate the total profit
    total_profit = (total_package_revenue + total_single_revenue) - total_cost
    result = total_profit
    return result

print(solution())
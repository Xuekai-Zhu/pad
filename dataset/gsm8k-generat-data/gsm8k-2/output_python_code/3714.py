def solution():
    """Sam bought a dozen boxes, each with 30 highlighter pens inside, for $10 each box. He rearranged five of these boxes into packages of six highlighters each and sold them for $3 per package. He sold the rest of the highlighters separately at the rate of three pens for $2. How much profit did he make in total, in dollars?"""
    boxes_bought = 12
    pens_per_box = 30
    box_price = 10
    package_size = 6
    package_price = 3
    separate_price = (2/3)*package_price
    total_cost = boxes_bought * box_price
    pen_count = boxes_bought * pens_per_box
    packaged_pens = 5 * pens_per_box
    remaining_pens = pen_count - packaged_pens
    packaged_sales = (5 * pens_per_box) / package_size * package_price
    separate_sales = (remaining_pens / 3) * separate_price
    total_sales = packaged_sales + separate_sales
    profit = total_sales - total_cost
    result = profit
    return result

print(solution())
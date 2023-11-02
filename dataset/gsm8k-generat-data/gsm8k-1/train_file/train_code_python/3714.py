def solution():
    """Sam bought a dozen boxes, each with 30 highlighter pens inside, for $10 each box. He rearranged five of these boxes into packages of six highlighters each and sold them for $3 per package. He sold the rest of the highlighters separately at the rate of three pens for $2. How much profit did he make in total, in dollars?"""
    boxes_bought = 12
    pens_per_box = 30
    cost_per_box = 10
    total_cost = boxes_bought * cost_per_box
    boxes_for_packages = 5
    pens_for_packages = boxes_for_packages * pens_per_box
    packages_made = pens_for_packages // 6
    price_per_package = 3
    income_from_packages = packages_made * price_per_package
    pens_for_individual_sale = (boxes_bought * pens_per_box) - pens_for_packages
    price_per_three_pens = 2
    pens_sold = pens_for_individual_sale // 3
    income_from_individual_sale = pens_sold * price_per_three_pens
    total_income = income_from_packages + income_from_individual_sale
    profit = total_income - total_cost
    return profit

print(solution())
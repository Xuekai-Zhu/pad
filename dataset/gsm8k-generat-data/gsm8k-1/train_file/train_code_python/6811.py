def solution():
    """Alice made 52 friendship bracelets over spring break to sell at school. It only cost her $3.00 in materials to make these bracelets. During the break, she gave 8 of her bracelets away. Back at school, she sells all of the remaining bracelets at $0.25 each. How much profit did she make 
    (money earned after paying initial costs) on the sale of her bracelets?"""
    num_bracelets = 52
    cost_materials = 3.00
    num_bracelets_given_away = 8
    num_bracelets_sold = num_bracelets - num_bracelets_given_away
    price_per_bracelet = 0.25
    revenue_from_bracelets_sold = num_bracelets_sold * price_per_bracelet
    profit = revenue_from_bracelets_sold - cost_materials
    result = profit
    return result

print(solution())
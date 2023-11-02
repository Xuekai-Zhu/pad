def solution():
    """Alice made 52 friendship bracelets over spring break to sell at school. It only cost her $3.00 in materials to make these bracelets. During the break, she gave 8 of her bracelets away. Back at school, she sells all of the remaining bracelets at $0.25 each. How much profit did she make (money earned after paying initial costs) on the sale of her bracelets?"""
    bracelets_made = 52
    materials_cost = 3.00
    bracelets_given_away = 8
    remaining_bracelets = bracelets_made - bracelets_given_away
    price_per_bracelet = 0.25
    total_earned = remaining_bracelets * price_per_bracelet
    profit = total_earned - materials_cost
    result = profit
    return result

print(solution())
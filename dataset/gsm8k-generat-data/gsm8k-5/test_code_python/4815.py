def solution():
    # Calculate how many bracelets Zayne sold for $5 each
    num_bracelets_5 = 60 / 5

    # Calculate how many bracelets Zayne sold at the discounted price
    num_bracelets_2_for_8 = (30 - num_bracelets_5) / 2

    # Calculate the total amount made from selling bracelets at both prices
    total_money = (num_bracelets_5 * 5) + (num_bracelets_2_for_8 * 4)
    result = total_money
    return result

print(solution())
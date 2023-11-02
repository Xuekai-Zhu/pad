def solution():
    # Define the bulk price and minimum spend
    bulk_price = 5
    min_spend = 40

    # Calculate the amount spent on honey before tax
    pre_tax_spend = (240 - 1 * (240 // 5)) - 40

    # Calculate the number of pounds purchased above the minimum spend
    pounds_above_min_spend = pre_tax_spend / bulk_price

    result = pounds_above_min_spend
    return result

print(solution())
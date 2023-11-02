def solution():
    coupe_price = 30000

    suv_price = 2 * coupe_price

    # Calculate the total amount of money made from both sales
    total_sales = coupe_price + suv_price

    # Calculate Melissa's commission
    commission_rate = 0.02
    commission = total_sales * commission_rate

    result = commission
    return result

print(solution())
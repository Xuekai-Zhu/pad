def solution():
    bulk_price = 5.00
    min_spend = 40.00
    tax_price = 1.00
    total_paid = 240.00

    # Calculate the total amount of honey purchased
    total_honey = (total_paid - min_spend) / (bulk_price + tax_price)

    # Calculate the amount by which the purchase exceeds the minimum spend
    excess = total_honey - (total_paid - min_spend) / bulk_price

    result = excess
    return result

print(solution())
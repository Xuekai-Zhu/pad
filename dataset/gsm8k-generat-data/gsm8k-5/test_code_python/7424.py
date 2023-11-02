def solution():
    bulk_price = 5  # Bulk price of honey is $5 per pound
    minimum_spend = 40  # Minimum spend before tax is $40
    tax = 1  # Tax on honey is $1 per pound
    paid_amount = 240  # Penny has paid $240 for honey

    # Calculate the amount of honey purchased before tax
    amount_of_honey = (paid_amount - minimum_spend) / (bulk_price + tax)

    # Calculate the amount of honey purchased in excess of the minimum spend
    excess_honey = amount_of_honey - (minimum_spend / (bulk_price + tax))
    result = excess_honey
    return result

print(solution())
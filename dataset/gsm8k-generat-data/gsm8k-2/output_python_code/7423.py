def solution():
    """In the honey shop, the bulk price of honey is $5 per pound and the minimum spend is $40 before tax. The honey is taxed at $1 per pound. If Penny has paid $240 for honey, by how many pounds has Penny’s purchase exceed the minimum spend?"""
    bulk_price = 5
    minimum_spend = 40
    tax = 1
    total_spent = 240
    pounds_purchased = (total_spent - tax*minimum_spend) / (bulk_price + tax)
    excess_pounds = pounds_purchased - (minimum_spend / (bulk_price + tax))
    result = excess_pounds
    return result

print(solution())
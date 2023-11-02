def solution():
    """In the honey shop, the bulk price of honey is $5 per pound and the minimum spend is $40 before tax. The honey is taxed at $1 per pound. If Penny has paid $240 for honey, by how many pounds has Penny’s purchase exceeded the minimum spend?"""
    bulk_price = 5
    minimum_spend = 40
    tax_per_pound = 1
    total_spend = 240
    pounds_of_honey = (total_spend - minimum_spend) / (bulk_price + tax_per_pound)
    excess_pounds = pounds_of_honey - minimum_spend / (bulk_price + tax_per_pound)
    result = excess_pounds
    return result

print(solution())
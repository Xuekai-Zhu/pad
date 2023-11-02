def solution():
    cans_per_case = 48  # The bulk warehouse offers 48 cans of sparkling water per case
    bulk_price = 12.00  # The bulk warehouse charges $12.00 per case
    grocery_cans = 12  # The local grocery store offers 12 cans of sparkling water per package
    grocery_price = 6.00  # The local grocery store charges $6.00 per package

    # Calculate the price per can at the bulk warehouse
    bulk_can_price = bulk_price / cans_per_case

    # Calculate the price per can at the grocery store
    grocery_can_price = grocery_price / grocery_cans

    # Calculate the price difference per can in cents
    price_diff_per_can = (grocery_can_price - bulk_can_price) * 100

    result = price_diff_per_can
    return result

print(solution())
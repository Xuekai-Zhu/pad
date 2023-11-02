def solution():
    cans_per_case = 48
    case_price = 12.0
    local_store_price = 6.0
    local_store_cans = 12

    # Calculate the cost per can at the bulk warehouse
    bulk_warehouse_can_price = case_price / cans_per_case

    # Calculate the cost per can at the local grocery store
    local_store_can_price = local_store_price / local_store_cans

    # Calculate the difference in price per can
    price_difference = (local_store_can_price - bulk_warehouse_can_price) * 100

    result = price_difference
    return result

print(solution())
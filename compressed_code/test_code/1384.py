def solution():
    
    case_size = 48
    case_price = 576
    unit_price_swap = 18
    unit_price_store = 25
    unit_price_remaining = 22
    sold_swap = 17
    sold_store = 10
    sold_remaining = case_size - sold_swap - sold_store
    
    revenue = (sold_swap * unit_price_swap) + (sold_store * unit_price_store) + (sold_remaining * unit_price_remaining)
    cost = case_price
    profit = revenue - cost
    result = profit
    return result

print(solution())
def solution():
    
    total_sales = 80
    necklace_price = 12
    necklace_count = 4
    necklace_sales = necklace_count * necklace_price
    ring_sales = total_sales - necklace_sales
    ring_count = 8
    ring_price = ring_sales / ring_count
    result = ring_price
    return result

print(solution())
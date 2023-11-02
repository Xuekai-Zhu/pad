def solution():
    
    necklaces_sold = 4
    rings_sold = 8
    total_sales = 80
    necklace_price = 12
    ring_price = (total_sales - (necklaces_sold * necklace_price)) / rings_sold
    result = ring_price
    return result

print(solution())
def solution():
    
    initial_stock = 200 / 2
    total_stock = initial_stock + 200
    sold_stock = total_stock * 3 / 4
    remaining_stock = total_stock - sold_stock
    remaining_stock += 300 - 150
    result = remaining_stock
    return result

print(solution())
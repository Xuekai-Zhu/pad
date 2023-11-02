def solution():
    
    initial_stock = 200
    fish_sold = 50
    remaining_stock = initial_stock - fish_sold
    spoiled_fish = remaining_stock / 3
    remaining_stock -= spoiled_fish
    new_stock = 200
    total_stock = remaining_stock + new_stock
    result = total_stock
    return result

print(solution())
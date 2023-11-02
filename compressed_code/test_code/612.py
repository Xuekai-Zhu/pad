def solution():
    
    initial_stock = 200
    sold_fish = 50
    remaining_fish = initial_stock - sold_fish
    spoiled_fish = remaining_fish / 3
    new_stock = 200
    total_fish = remaining_fish - spoiled_fish + new_stock
    result = total_fish
    return result

print(solution())
def solution():
    initial_stock = 200
    sold_fish = 50
    spoiled_fish = (initial_stock - sold_fish) / 3
    remaining_fish = initial_stock - sold_fish - spoiled_fish
    new_stock = 200
    total_stock = remaining_fish + new_stock
    result = total_stock
    return result

print(solution())
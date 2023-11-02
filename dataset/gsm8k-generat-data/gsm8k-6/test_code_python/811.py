def solution():
    initial_stock = 200  # initial stock of fish
    sold_fish = 50  # number of fish sold
    remaining_stock = initial_stock - sold_fish  # remaining stock of fish after selling
    spoiled_fish = remaining_stock // 3  # number of fish that get spoiled
    remaining_stock -= spoiled_fish  # subtract the spoiled fish from the remaining stock
    new_stock = 200  # new stock of fish
    total_stock = remaining_stock + new_stock  # total stock of fish
    result = total_stock
    return result

print(solution())
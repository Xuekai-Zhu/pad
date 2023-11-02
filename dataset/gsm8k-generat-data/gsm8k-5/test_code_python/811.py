def solution():
    initial_stock = 200  # Steve has a stock of 200 fish
    sold_fish = 50  # Steve sells 50 fish
    remaining_stock = initial_stock - sold_fish  # Steve has a remaining stock of 150 fish
    spoiled_fish = remaining_stock // 3  # One third of the remaining fish become spoiled
    remaining_stock -= spoiled_fish  # Steve subtracts the spoiled fish from the remaining stock
    new_stock = 200  # Steve receives a new stock of 200 fish
    total_stock = remaining_stock + new_stock  # Steve adds the remaining stock and new stock to get the total stock

    result = total_stock
    return result

print(solution())
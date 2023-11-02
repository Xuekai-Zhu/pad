def solution():
    """Steve owns a lake shop that sells fish. He has a stock of 200 fish. He sells 50 fish and because his refrigerators stop working a third of the remaining fish become spoiled. A new stock of 200 more fish arrives. How many fish does he have in stock now?"""
    initial_stock = 200
    sold_fish = 50
    remaining_fish = initial_stock - sold_fish
    spoiled_fish = remaining_fish / 3
    new_stock = 200
    total_fish = remaining_fish - spoiled_fish + new_stock
    result = total_fish
    return result

print(solution())
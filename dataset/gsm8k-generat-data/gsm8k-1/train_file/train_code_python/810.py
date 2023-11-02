def solution():
    """Steve owns a lake shop that sells fish. He has a stock of 200 fish. He sells 50 fish and because his refrigerators stop working a third of the remaining fish become spoiled. A new stock of 200 more fish arrives. How many fish does he have in stock now?"""
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
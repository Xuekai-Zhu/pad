def solution():
    """Steve owns a lake shop that sells fish. He has a stock of 200 fish. 
    He sells 50 fish and because his refrigerators stop working a third of the remaining fish become spoiled. 
    A new stock of 200 more fish arrives. How many fish does he have in stock now?"""
    
    # Initial stock of fish
    start_stock = 200
    
    # Fish sold
    sold_fish = 50
    
    # Calculate remaining fish after selling
    remaining_fish = start_stock - sold_fish
    
    # Calculate number of spoiled fish
    spoiled_fish = remaining_fish // 3
    
    # Calculate final stock after arrival of new fish
    final_stock = remaining_fish - spoiled_fish + 200
    
    # Display final stock
    result = final_stock
    return result

print(solution())
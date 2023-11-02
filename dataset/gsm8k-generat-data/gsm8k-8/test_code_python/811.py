def solution():
    # Define the initial stock of fish
    initial_stock = 200

    # Sell 50 fish
    remaining_stock = initial_stock - 50

    # Calculate the number of spoiled fish
    spoiled_fish = remaining_stock / 3

    # Subtract the number of spoiled fish from the remaining stock
    remaining_stock -= spoiled_fish

    # Add the new stock of 200 fish
    total_stock = remaining_stock + 200
    result = total_stock
    return result

print(solution())
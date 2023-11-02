def solution():
    # Define the number of chocolate and mango ice creams sold
    sold_chocolate = (3/5) * 50
    sold_mango = (2/3) * 54

    # Calculate the number of unsold ice creams
    unsold_chocolate = 50 - sold_chocolate
    unsold_mango = 54 - sold_mango
    total_unsold = unsold_chocolate + unsold_mango
    result = total_unsold
    return result

print(solution())
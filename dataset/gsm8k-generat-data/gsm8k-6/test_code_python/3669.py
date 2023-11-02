def solution():
    # Calculate the number of chocolate and mango ice creams sold
    sold_chocolate = (3/5) * 50
    sold_mango = (2/3) * 54

    # Calculate the total number of ice creams not sold
    not_sold = 50 - sold_chocolate + 54 - sold_mango
    result = not_sold
    return result

print(solution())
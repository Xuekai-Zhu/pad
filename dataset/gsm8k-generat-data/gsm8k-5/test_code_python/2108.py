def solution():
    # Quantity bought on Monday
    monday_quantity = 15

    # Quantity bought on Tuesday
    tuesday_quantity = 3 * monday_quantity

    # Quantity bought on Wednesday
    wednesday_quantity = 4 * tuesday_quantity

    # Calculate the total quantity bought
    total_quantity = monday_quantity + tuesday_quantity + wednesday_quantity
    result = total_quantity
    return result

print(solution())
def solution():
    original_shirt_price = 60
    original_jacket_price = 90
    discount = 0.2  # 20% discount

    # Calculate the new price of a shirt after the discount
    new_shirt_price = original_shirt_price * (1 - discount)

    # Calculate the new price of a leather jacket after the discount
    new_jacket_price = original_jacket_price * (1 - discount)

    # Calculate the total cost of 5 shirts
    total_shirts_cost = new_shirt_price * 5

    # Calculate the total cost of 10 leather jackets
    total_jackets_cost = new_jacket_price * 10

    # Calculate the total cost of all items
    total_cost = total_shirts_cost + total_jackets_cost
    result = total_cost
    return result

print(solution())
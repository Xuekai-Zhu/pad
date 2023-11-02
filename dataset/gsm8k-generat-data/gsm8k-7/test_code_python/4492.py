def solution():
    num_skirts = 2
    skirt_price = 13.0

    num_blouses = 3
    blouse_price = 6.0

    total_paid = 100.0

    # Calculate the total cost of all skirts
    total_skirt_cost = num_skirts * skirt_price

    # Calculate the total cost of all blouses
    total_blouse_cost = num_blouses * blouse_price

    # Calculate the total cost of all items
    total_cost = total_skirt_cost + total_blouse_cost

    # Calculate the change she received
    change = total_paid - total_cost
    result = change
    return result

print(solution())
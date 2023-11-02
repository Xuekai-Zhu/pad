def solution():
    hamburger_price = 4
    onion_rings_price = 2
    smoothie_price = 3
    total_paid = 20

    # Calculate the total cost of the lunch
    total_cost = hamburger_price + onion_rings_price + smoothie_price

    # Calculate the change that Morgan will receive
    change = total_paid - total_cost
    result = change
    return result

print(solution())
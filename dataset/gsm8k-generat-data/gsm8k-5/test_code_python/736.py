def solution():
    samosas_cost = 3 * 2  # Hilary bought 3 samosas at $2 each
    pakoras_cost = 4 * 3  # Hilary bought 4 orders of pakoras at $3 each
    lassi_cost = 2  # Hilary bought a mango lassi for $2
    subtotal = samosas_cost + pakoras_cost + lassi_cost  # Calculate the subtotal
    tax = subtotal * 0.08  # Tax is 8% of the subtotal
    tip = subtotal * 0.25  # Tip is 25% of the subtotal
    total_cost = subtotal + tax + tip  # Calculate the total cost

    result = round(total_cost, 2)  # Round the total cost to 2 decimal places
    return result

print(solution())
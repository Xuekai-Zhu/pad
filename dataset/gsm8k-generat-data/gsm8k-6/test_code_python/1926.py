def solution():
    # Calculate the cost per pouch in cents
    total_pouches = 10 * 6  # 10 boxes with 6 pouches each
    total_cost = 12 * 100  # convert dollars to cents
    cost_per_pouch = total_cost / total_pouches
    result = cost_per_pouch
    return result

# Alternatively, we can simplify the calculation using integer division:
# cost_per_pouch = (12 * 100) // (10 * 6)
# The double slashes indicate integer division, which truncates any decimals.

print(solution())
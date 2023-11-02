def solution():
    """At the Delicious Delhi restaurant, Hilary bought three samosas at $2 each and four orders of pakoras, at $3 each, and a mango lassi, for $2. She left a 25% tip. How much did the meal cost Hilary, with tax, in dollars?"""
    samosas_cost = 3 * 2
    pakoras_cost = 4 * 3
    lassi_cost = 2
    subtotal = samosas_cost + pakoras_cost + lassi_cost
    tip = 0.25 * subtotal
    total_cost = subtotal + tip
    result = total_cost
    return result

print(solution())
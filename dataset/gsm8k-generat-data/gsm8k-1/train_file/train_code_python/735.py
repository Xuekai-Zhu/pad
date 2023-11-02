def solution():
    """At the Delicious Delhi restaurant, Hilary bought three samosas at $2 each 
    and four orders of pakoras, at $3 each, and a mango lassi, for $2. 
    She left a 25% tip. How much did the meal cost Hilary, with tax, in dollars?"""
    samosas = 3
    samosa_cost = 2
    pakoras = 4
    pakora_cost = 3
    lassi_cost = 2
    sub_total = (samosas * samosa_cost) + (pakoras * pakora_cost) + lassi_cost
    tip = sub_total * 0.25
    total_cost = sub_total + tip
    result = total_cost
    return result

print(solution())
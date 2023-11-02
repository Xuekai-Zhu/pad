def solution():
    """Sally went to the seashore for vacation. Her parents gave her $10 to buy whatever she wanted. At the trinket shop, taffy was on sale for "Buy 1 pound at $3, get 1 pound 1/2 off." She scooped up 2 pounds. She also bought a mixed bag of seashells for $1.50 and 4 magnets that were $0.25 each. How much money does Sally have left?"""
    starting_amount = 10
    taffy_price_per_pound = 3
    taffy_weight = 2.5 # 1 pound at $3, get 1/2 pound off
    taffy_cost = taffy_weight * taffy_price_per_pound
    seashells_cost = 1.5
    magnets_cost = 4 * 0.25
    total_cost = taffy_cost + seashells_cost + magnets_cost
    remaining_amount = starting_amount - total_cost
    result = remaining_amount
    return result

print(solution())
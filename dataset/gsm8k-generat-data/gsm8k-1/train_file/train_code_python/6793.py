def solution():
    """Francis and Kiera had breakfast at a cafe. Muffins cost $2 each, and fruit cups cost $3 each. 
    Francis had 2 muffins and 2 fruit cups. Kiera had 2 muffins and 1 fruit cup. How much did their breakfast cost?"""
    muffin_cost = 2
    fruit_cost = 3
    francis_muffins = 2
    francis_fruit = 2
    kiera_muffins = 2
    kiera_fruit = 1
    francis_total = (francis_muffins * muffin_cost) + (francis_fruit * fruit_cost)
    kiera_total = (kiera_muffins * muffin_cost) + (kiera_fruit * fruit_cost)
    total_cost = francis_total + kiera_total
    result = total_cost
    return result

print(solution())
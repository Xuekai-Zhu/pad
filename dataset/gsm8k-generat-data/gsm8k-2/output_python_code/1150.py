def solution():
    """Kobe and Pau went to a restaurant. Kobe ordered five pieces of fried chicken, and Pau ordered twice as much fried chicken as Kobe did. If they order another set of fried chicken, how many pieces of fried chicken will Pau have eaten in all?"""
    kobe_order = 5
    pau_order = 2 * kobe_order
    total_order = kobe_order + pau_order + 5
    result = pau_order + total_order
    return result

print(solution())
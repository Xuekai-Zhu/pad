def solution():
    """Deandre caught 3 tunas last Monday, the first tuna he caught weighs 56 kilograms,
    the second tuna he caught weighs 46 kilograms, and the last tuna he caught weighs 26 kilograms.
    If a kilogram of tuna costs $0.50, how much will he earn after selling all the tunas to the market?"""
    tuna1_weight = 56
    tuna2_weight = 46
    tuna3_weight = 26
    cost_per_kilo = 0.5
    total_weight = tuna1_weight + tuna2_weight + tuna3_weight
    earnings = total_weight * cost_per_kilo
    result = earnings
    return result

print(solution())
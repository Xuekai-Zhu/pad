def solution():
    """Jonah bought 6 pineapples for $3 each. Each pineapple could be cut into 12 pineapple rings. He sold 4 pineapple rings for $5 each. How much profit did Jonah make?"""
    pineapples_cost = 6 * 3
    pineapple_rings = 6 * 12
    pineapples_income = 4 * 5 * (pineapple_rings // 4)
    profit = pineapples_income - pineapples_cost
    result = profit
    return result

print(solution())
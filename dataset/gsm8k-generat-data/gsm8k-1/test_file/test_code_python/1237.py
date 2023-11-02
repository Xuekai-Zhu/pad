def solution():
    """Rose bought five dozens of eggs for $2.40 a dozen. She will sell it for $1 for 3 eggs. How much will be Rose's profit?"""
    dozen_price = 2.40
    eggs_per_dozen = 12
    total_eggs = 5 * eggs_per_dozen
    cost_price = 5 * dozen_price
    selling_price = (total_eggs // 3) * 1
    profit = selling_price - cost_price
    result = profit
    return result

print(solution())
def solution():
    """Jenny makes and freezes pans of lasagna all week so she can sell them at the market on the weekend. It costs Jenny $10.00 in ingredients to make 1 pan of lasagna. If she makes and sells 20 pans over the weekend at $25.00 apiece, how much does she make after factoring in expenses?"""
    cost_per_pan = 10
    sale_price_per_pan = 25
    total_profit = (sale_price_per_pan - cost_per_pan) * 20
    result = total_profit
    return result

print(solution())
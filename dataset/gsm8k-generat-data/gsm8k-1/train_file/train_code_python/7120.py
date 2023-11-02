def solution():
    """Jenny makes and freezes pans of lasagna all week so she can sell them at the market on the weekend. It costs Jenny $10.00 in ingredients to make 1 pan of lasagna. If she makes and sells 20 pans over the weekend at $25.00 apiece, how much does she make after factoring in expenses?"""
    cost_per_pan = 10
    selling_price_per_pan = 25
    pans_sold = 20
    total_cost = cost_per_pan * pans_sold
    total_revenue = selling_price_per_pan * pans_sold
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())
def solution():
    """Mac loves the shape of quarters and is willing to trade money for them, even if he loses value. He tells his brother that he will trade him 3 dimes for a quarter or 7 nickels. He trades for 20 quarters with dimes and 20 quarters with nickels. How many dollars did Mac lose?"""
    dimes_per_quarter = 3
    nickels_per_quarter = 7
    quarters_traded = 20
    total_dimes_traded = quarters_traded * dimes_per_quarter
    total_nickels_traded = quarters_traded * nickels_per_quarter
    total_dollars_lost = (total_dimes_traded * 0.1) + (total_nickels_traded * 0.05) - (quarters_traded * 0.25)
    result = total_dollars_lost
    return round(result, 2)

print(solution())
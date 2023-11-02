def solution():
    """Jame has 60 bars of gold. He uses 10% of them to pay for tax and then loses half of what is left in divorce. How many gold bars does he have left?"""
    total_bars = 60
    tax_bars = total_bars * 0.1
    remaining_bars = total_bars - tax_bars
    divorce_bars = remaining_bars / 2
    final_bars = remaining_bars - divorce_bars
    result = final_bars
    return result

print(solution())
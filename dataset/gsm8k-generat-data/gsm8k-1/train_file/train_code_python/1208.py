def solution():
    """Jame has 60 bars of gold. He uses 10% of them to pay for tax and then loses half of what is left in divorce. How many gold bars does he have left?"""
    initial_bars = 60
    tax_bars = initial_bars * 0.1
    remaining_bars = initial_bars - tax_bars
    remaining_bars /= 2
    result = remaining_bars
    return result

print(solution())
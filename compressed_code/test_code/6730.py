def solution():
    
    initial_bars = 60
    tax_bars = initial_bars * 0.1
    remaining_bars = initial_bars - tax_bars
    remaining_bars /= 2
    result = remaining_bars
    return result

print(solution())
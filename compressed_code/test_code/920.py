def solution():
    
    total_bars = 60
    tax_bars = total_bars * 0.1
    remaining_bars = total_bars - tax_bars
    divorce_bars = remaining_bars / 2
    final_bars = remaining_bars - divorce_bars
    result = final_bars
    return result

print(solution())
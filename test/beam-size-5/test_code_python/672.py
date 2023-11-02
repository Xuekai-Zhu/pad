def solution():
    
    total_investment = 1200
    dylan_investment = (2/5) * total_investment
    remaining_investment = total_investment - dylan_investment
    frances_investment = (2/3) * remaining_investment
    Skyler_investment = remaining_investment - frances_investment
    result = Skyler_investment
    return result

print(solution())
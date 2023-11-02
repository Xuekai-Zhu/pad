def solution():
    
    total_judges = 40
    under_thirty_percent = 0.1
    thirty_to_fifty_percent = 0.6
    under_thirty = total_judges * under_thirty_percent
    thirty_to_fifty = total_judges * thirty_to_fifty_percent
    over_fifty = total_judges - under_thirty - thirty_to_fifty
    result = over_fifty
    return result

print(solution())
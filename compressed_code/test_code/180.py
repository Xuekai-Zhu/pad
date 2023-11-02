def solution():
    
    normal_price = 34
    discount_per_issue = 0.25
    total_issues = 18 * 2
    promotional_price = normal_price - (discount_per_issue * total_issues)
    difference = normal_price - promotional_price
    result = difference
    return result

print(solution())
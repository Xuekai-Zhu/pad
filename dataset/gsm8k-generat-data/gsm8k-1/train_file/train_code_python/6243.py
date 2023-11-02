def solution():
    """Tony decided to rent a small cottage. The master bedroom and bath totaled 500 sq ft. The 2 guest bedrooms were 200 sq ft each. And the kitchen, guest bath and living area totaled 600 sq ft. If Tony spends $3,000 a month on rent, how much money is he spending per sq ft of house?"""
    total_sq_ft = 500 + (2 * 200) + 600
    cost_per_sq_ft = 3000 / total_sq_ft
    result = cost_per_sq_ft
    return result

print(solution())
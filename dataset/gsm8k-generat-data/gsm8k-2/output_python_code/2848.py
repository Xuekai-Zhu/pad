def solution():
    """For breakfast, Anna bought a bagel for $0.95 and a glass of orange juice for $0.85. At lunch, Anna spent $4.65 on a sandwich and $1.15 on a carton of milk. How much more money did Anna spend on lunch than on breakfast?"""
    breakfast_total = 0.95 + 0.85
    lunch_total = 4.65 + 1.15
    difference = lunch_total - breakfast_total
    result = difference
    return result

print(solution())
def solution():
    """Manny signed up for Karate classes for $60. His parents tell him that if his classes end up costing more than $10 per class, then they won't sign him up again. If there are 10 total classes, how many can he miss before they don't sign him up again?"""
    total_cost = 60
    total_classes = 10
    max_cost_per_class = 10
    max_classes_missed = (total_cost - (max_cost_per_class * total_classes)) / max_cost_per_class
    result = max_classes_missed
    return result

print(solution())
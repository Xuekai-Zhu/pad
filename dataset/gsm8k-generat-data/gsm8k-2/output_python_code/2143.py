def solution():
    """Sharon’s vacation rental has a Keurig coffee machine. She will be there for 40 days. She has 3 cups of coffee (3 coffee pods) every morning. Her coffee pods come 30 pods to a box for $8.00. How much will she spend on coffee to last her for the entire vacation?"""
    days = 40
    pods_per_day = 3
    pods_per_box = 30
    cost_per_box = 8.00
    total_pods = days * pods_per_day
    boxes_needed = total_pods / pods_per_box
    total_cost = boxes_needed * cost_per_box
    result = total_cost
    return result

print(solution())
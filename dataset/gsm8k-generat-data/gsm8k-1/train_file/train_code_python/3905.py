def solution():
    """Verna weighs 17 pounds more than Haley, and Verna weighs half as much as Sherry.
    If Haley weighs 103 pounds, how many pounds do Verna and Sherry weigh together?"""
    haley_weight = 103
    verna_weight = haley_weight + 17
    sherry_weight = verna_weight * 2
    total_weight = verna_weight + sherry_weight
    result = total_weight
    return result

print(solution())
def solution():
    """Mark was unwell for 3 months, during which he lost 10 pounds per month. If his final weight was 70 pounds, what was his initial weight?"""
    weight_loss_per_month = 10
    months_unwell = 3
    final_weight = 70
    initial_weight = final_weight + (weight_loss_per_month * months_unwell)
    result = initial_weight
    return result

print(solution())
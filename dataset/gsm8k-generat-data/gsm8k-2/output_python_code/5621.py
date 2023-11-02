def solution():
    """Michael wants to lose 10 pounds by June. He lost 3 pounds in March and 4 pounds in April. How much weight does he have to lose in May to meet his goal?"""
    goal_weight_loss = 10
    weight_loss_so_far = 3 + 4
    remaining_weight_loss = goal_weight_loss - weight_loss_so_far
    result = remaining_weight_loss
    return result

print(solution())
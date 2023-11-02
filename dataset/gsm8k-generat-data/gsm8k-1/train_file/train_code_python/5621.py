def solution():
    """Michael wants to lose 10 pounds by June. He lost 3 pounds in March and 4 pounds in April. How much weight does he have to lose in May to meet his goal?"""
    goal_weight_loss = 10
    weight_loss_so_far = 3 + 4
    weight_left_to_lose = goal_weight_loss - weight_loss_so_far
    result = weight_left_to_lose
    return result

print(solution())
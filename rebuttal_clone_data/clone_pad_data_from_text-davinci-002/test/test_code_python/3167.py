def solution():
    goal_weight_loss = 10
    weight_loss_march = 3
    weight_loss_april = 4
    weight_loss_may = goal_weight_loss - (weight_loss_march + weight_loss_april)
    result = weight_loss_may
    return result

print(solution())
def solution():
    initial_weight = 250
    weight_loss_week1 = 3
    weight_loss_week2 = 3
    weight_loss_week3 = 3
    weight_loss_week4 = 3
    weight_loss_week5 = 2
    weight_loss_week6 = 2
    weight_loss_week7 = 2
    weight_loss_week8 = 2
    weight_loss_week9 = 2
    weight_loss_week10 = 2
    weight_loss_week11 = 2
    weight_loss_week12 = 2
    final_weight = initial_weight - (weight_loss_week1 + weight_loss_week2 + weight_loss_week3 + weight_loss_week4 + weight_loss_week5 + weight_loss_week6 + weight_loss_week7 + weight_loss_week8 + weight_loss_week9 + weight_loss_week10 + weight_loss_week11 + weight_loss_week12)
    result = final_weight
    
    return result

print(solution())
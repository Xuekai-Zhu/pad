def solution():
    """John weighs 220 pounds when he starts exercising. He manages to lose 10% of his body weight. He then gains back 2 pounds. How much does he weigh at the end?"""
    starting_weight = 220
    weight_loss_percent = 10
    weight_loss = starting_weight * (weight_loss_percent / 100)
    current_weight = starting_weight - weight_loss + 2
    result = current_weight
    return result

print(solution())
def solution():
    """Andy started out the year weighing 156 pounds. He then grew 3 inches and gained 36 pounds. Andy wasn't happy with his weight and decided to exercise. Over the next 3 months, he lost an eighth of his weight every month. How much less does Andy weigh now than at the beginning of the year?"""
    initial_weight = 156
    growth_weight = 36
    current_weight = initial_weight + growth_weight
    monthly_loss = current_weight / 8
    total_loss = 3 * monthly_loss
    new_weight = current_weight - total_loss
    weight_difference = initial_weight - new_weight
    result = weight_difference
    return result

print(solution())
def solution():
    """Andy started out the year weighing 156 pounds. He then grew 3 inches and gained 36 pounds.
    Over the next 3 months, he lost an eighth of his weight every month. How much less does Andy weigh now than at the beginning of the year?"""
    initial_weight = 156
    height_increase = 3
    weight_gain = 36
    new_height = height_increase + 72  # Assuming Andy started at 69 inches
    bmi = (initial_weight + weight_gain) / (new_height ** 2) * 703
    for i in range(3):
        weight_loss = (1 / 8) * initial_weight
        initial_weight -= weight_loss
    weight_difference = initial_weight - (initial_weight + weight_gain)  # Difference in weight from start of year
    result = weight_difference
    return result

print(solution())
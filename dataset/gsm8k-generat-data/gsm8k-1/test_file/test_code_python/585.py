def solution():
    """If Martin eats Cheerios every day for breakfast, he'll lose 1.25 pounds/week. If he eats donuts every day for breakfast, he'll gain 1.75 pounds/week. What will be the difference in his weight at the end of 5 weeks between the two breakfast options?"""
    cheerios_weight_loss = -1.25
    donuts_weight_gain = 1.75
    weeks = 5
    weight_difference = (cheerios_weight_loss - donuts_weight_gain) * weeks
    result = weight_difference
    return result

print(solution())
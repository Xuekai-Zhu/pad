def solution():
    """Jamaal is at the gym. He has been using an 8-pound weight. He increases the weight that he uses by 50%. It turns out to be too heavy, so he uses a weight two pounds lighter than that. What is the weight, in pounds, that he now uses?"""
    initial_weight = 8
    percent_increase = 50
    new_weight = initial_weight * (1 + (percent_increase / 100))
    final_weight = new_weight - 2
    result = final_weight
    return result

print(solution())
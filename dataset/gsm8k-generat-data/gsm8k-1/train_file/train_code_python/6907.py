def solution():
    """
    Before James starts the strength phase training of his cycle he has a powerlifting total of 2200 pounds at a bodyweight 
    of 245 pounds. He manages to gain 15% on his total and 8 pounds of body weight. What is the ratio of his lifting total 
    to bodyweight?
    """
    initial_total = 2200
    initial_weight = 245
    total_gain = initial_total * 0.15
    weight_gain = 8
    final_total = initial_total + total_gain
    final_weight = initial_weight + weight_gain
    ratio = final_total / final_weight
    result = ratio
    return result

print(solution())
def solution():
    """John injures his shoulder while lifting weights. After the injury, his bench press goes down 80%. After a bit of training, he manages to triple the weight he can bench. If he started with a 500-pound bench press, what is it now?"""
    initial_weight = 500
    decrease_percent = 80
    decreased_weight = initial_weight * (1 - (decrease_percent / 100))
    final_weight = decreased_weight * 3
    result = final_weight
    return result

print(solution())
def solution():
    """Tom uses 10 weight plates each weighing 30 pounds on an exercise machine. This exercise machine uses special technology to make the weights 20% heavier on the lowering portion. How heavy did the weights feel when being lowered?"""
    num_plates = 10
    plate_weight = 30
    weight_increase = 0.2
    lowered_weight = (1 + weight_increase) * plate_weight
    total_weight_lowered = num_plates * lowered_weight
    result = total_weight_lowered
    return result

print(solution())
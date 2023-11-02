def solution():
    """Tom uses 10 weight plates each weighing 30 pounds on an exercise machine. This exercise machine uses special technology to make the weights 20% heavier on the lowering portion. How heavy did the weights feel when being lowered?"""
    weight_plate = 30
    total_weight = weight_plate * 10
    added_weight = total_weight * 0.2
    lowered_weight = total_weight + added_weight
    result = lowered_weight
    return result

print(solution())
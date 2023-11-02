def solution():
    """Tom uses 10 weight plates each weighing 30 pounds on an exercise machine. This exercise machine uses special technology to make the weights 20% heavier on the lowering portion. How heavy did the weights feel when being lowered?"""
    number_of_plates = 10
    weight_of_plates = 30
    percent_increase = 20
    increase_amount = weight_of_plates * (percent_increase / 100)
    total_weight = number_of_plates * (weight_of_plates + increase_amount)
    result = total_weight
    return result

print(solution())
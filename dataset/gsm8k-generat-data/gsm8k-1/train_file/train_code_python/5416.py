def solution():
    """Mary tried to improve her health by changing her diet, but her weight bounced like a yo-yo. At first, she dropped a dozen pounds. Then, she added back twice the weight that she initially lost. Then, she dropped three times more weight than she initially had lost. But finally, she gained back half of a dozen pounds. If she weighed 99 pounds at the start of her change in diet, what was her final weight, in pounds?"""
    initial_weight = 99
    first_loss = 12
    first_gain = first_loss * 2
    second_loss = first_loss * 3
    final_gain = 6 / 2
    
    net_loss = first_loss - first_gain + second_loss - final_gain
    
    final_weight = initial_weight - net_loss
    
    result = final_weight
    
    return result

print(solution())
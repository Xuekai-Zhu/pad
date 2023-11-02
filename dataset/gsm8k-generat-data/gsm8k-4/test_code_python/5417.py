def solution():
    """Mary tried to improve her health by changing her diet, but her weight bounced like a yo-yo. At first, she dropped a dozen pounds. Then, she added back twice the weight that she initially lost. Then, she dropped three times more weight than she initially had lost. But finally, she gained back half of a dozen pounds. If she weighed 99 pounds at the start of her change in diet, what was her final weight, in pounds?"""
    # Define the initial weight of Mary
    initial_weight = 99
    
    # Calculate the weight after dropping a dozen pounds
    weight1 = initial_weight - 12
    
    # Calculate the weight after adding back twice the weight initially lost
    weight2 = weight1 + (2 * 12)
    
    # Calculate the weight after dropping three times more weight than initially lost
    weight3 = weight2 - (3 * 12)
    
    # Calculate the weight after gaining back half of a dozen pounds
    final_weight = weight3 + 6
    
    result = final_weight
    return result

print(solution())
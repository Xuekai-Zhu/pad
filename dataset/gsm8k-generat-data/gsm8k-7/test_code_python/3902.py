def solution():
    butter_per_cup = 2  # ounces
    coconut_oil_per_cup = 2  # ounces
    remaining_butter = 4  # ounces
    baking_mix = 6  # cups
    
    # Calculate the maximum amount of butter the chef can use
    max_butter = remaining_butter // butter_per_cup * butter_per_cup
    
    # Calculate the amount of baking mix that can be used with the remaining butter
    mix_with_butter = max_butter / butter_per_cup
    
    # Calculate the remaining amount of baking mix that needs to use coconut oil
    mix_with_oil = baking_mix - mix_with_butter
    
    # Calculate the amount of coconut oil needed
    coconut_oil = mix_with_oil * coconut_oil_per_cup
    
    result = coconut_oil
    return result

print(solution())
def solution():
    # Calculate the total amount earned from selling potato bundles
    num_potato_bundles = 250 // 25  # divide number of potatoes by 25 to get number of bundles
    total_earned_potatoes = num_potato_bundles * 1.9  # multiply number of bundles by price per bundle
    
    # Calculate the total amount earned from selling carrot bundles
    num_carrot_bundles = 320 // 20  # divide number of carrots by 20 to get number of bundles
    total_earned_carrots = num_carrot_bundles * 2  # multiply number of bundles by price per bundle
    
    # Calculate the total amount earned from selling all harvested crops
    total_earned = total_earned_potatoes + total_earned_carrots
    result = total_earned
    return result

print(solution())
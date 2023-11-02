def solution():
    initial_shampoo = 10
    dad_uses_per_day = 1
    
    hot_sauce_per_day = 0.5
    
    # Calculate the remaining shampoo after 4 days
    remaining_shampoo = initial_shampoo - (dad_uses_per_day * 4)
    
    # Calculate the total amount of hot sauce added in 4 days
    total_hot_sauce = hot_sauce_per_day * 4
    
    # Calculate the percentage of the liquid in the bottle that is hot sauce
    percentage_hot_sauce = (total_hot_sauce / (initial_shampoo - remaining_shampoo)) * 100
    
    result = percentage_hot_sauce
    return result

print(solution())
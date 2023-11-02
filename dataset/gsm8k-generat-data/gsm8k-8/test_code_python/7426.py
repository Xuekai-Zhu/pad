def solution():
    # Calculate the total remaining apples after juice and restaurant
    remaining_apples = 405 - 90 - 60
    
    # Calculate the total number of bags sold
    total_bags_sold = remaining_apples / 5
    
    # Calculate the price per bag
    price_per_bag = 408 / total_bags_sold
    
    result = price_per_bag
    return result

print(solution())
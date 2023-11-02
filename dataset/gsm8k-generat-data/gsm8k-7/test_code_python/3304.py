def solution():
    num_apples = 15
    apple_orange_ratio = 4
    num_oranges = num_apples / apple_orange_ratio
    
    # Calculate the total number of fruits in the basket
    total_fruits = num_apples + num_oranges
    
    # Calculate the quantity of each fruit that Emiliano will consume
    apple_quantity = (2/3) * num_apples
    orange_quantity = (2/3) * num_oranges
    
    # Calculate the total number of fruits that Emiliano will consume
    total_consumed = apple_quantity + orange_quantity
    result = total_consumed
    return result

print(solution())
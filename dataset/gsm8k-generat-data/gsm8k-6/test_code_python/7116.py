def solution():
    # Calculate the total weight of all the chocolate eggs
    total_weight = 12 * 10  # each chocolate egg weighs 10 ounces

    # Calculate the number of chocolate eggs in each of the remaining 3 boxes
    remaining_boxes = 3
    eggs_per_box = 12 // remaining_boxes  

    # Calculate the weight of the remaining chocolate eggs
    remaining_weight = eggs_per_box * 10 * remaining_boxes  # each chocolate egg weighs 10 ounces
    
    result = remaining_weight
    return result

print(solution())
def solution():
    # Calculate the weight of one plate in pounds
    weight_plate = 10/16  # 10 ounces is equivalent to 10/16 pounds
    
    # Calculate the weight of 38 plates in pounds
    weight_38_plates = weight_plate * 38
    
    # Calculate the difference between the weight of 38 plates and the maximum weight of a box
    weight_difference = (weight_38_plates - 20)
    
    # Calculate the number of plates that need to be removed to meet the maximum weight limit
    plates_removed = weight_difference / weight_plate
    
    # Round up to the nearest whole number of plates
    plates_removed = round(plates_removed + 0.5)
    
    result = plates_removed
    return result

print(solution())
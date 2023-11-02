def solution():
    # Calculate the remaining tomatoes after Saturday's sales and Sunday's loss
    remaining_tomatoes = 1000 - 300 - 200

    # Calculate the weight of the second shipment
    second_shipment = 2 * 1000

    # Calculate the total weight of tomatoes on Tuesday
    total_weight = remaining_tomatoes + second_shipment
    
    result = total_weight
    return result

print(solution())
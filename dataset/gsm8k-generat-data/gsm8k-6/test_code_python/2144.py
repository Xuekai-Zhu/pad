def solution():
    # Calculate the number of coffee pods Sharon will need for her entire vacation
    total_pods_needed = 3 * 40  

    # Calculate the number of boxes of coffee pods needed
    boxes_needed = total_pods_needed / 30  
    if boxes_needed.is_integer():
        boxes_needed = int(boxes_needed)
    else:
        boxes_needed = int(boxes_needed) + 1

    # Calculate the total cost of the coffee pods
    total_cost = boxes_needed * 8.00
    result = total_cost
    return result

print(solution())
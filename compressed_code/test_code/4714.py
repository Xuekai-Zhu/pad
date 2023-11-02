def solution():
    
    box_size = 20
    num_boxes = 12
    total_samples = box_size * num_boxes
    leftover_samples = 5
    num_customers = total_samples - leftover_samples
    result = num_customers
    return result

print(solution())
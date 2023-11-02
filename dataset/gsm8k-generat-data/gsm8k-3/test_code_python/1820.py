def solution():
    """Nida has 50 chocolates in which some are in 3 filled boxes and 5 pieces are not in a box. 
    Her friend brought 25 pieces of chocolates. If all chocolates must be placed in a box, 
    how many more boxes do they need?"""
    
    # Calculate the total number of chocolates
    total_chocolates = 50 + 25
    
    # Calculate the number of chocolates in boxes
    chocolates_in_boxes = 50 - 5
    
    # Calculate the number of boxes needed
    boxes_needed = (total_chocolates - chocolates_in_boxes) / 3
    
    # Round up to the nearest integer
    boxes_needed = math.ceil(boxes_needed)
    
    # Display the number of boxes needed
    result = boxes_needed
    return result

print(solution())
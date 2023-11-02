def solution():
    room_length = 16
    room_width = 20
    total_sq_ft = room_length * room_width
    flooring_per_box = 10
    flooring_complete = 250
    
    # Calculate the remaining sq ft of flooring needed
    remaining_sq_ft = total_sq_ft - flooring_complete
    
    # Calculate the number of boxes needed to complete the job
    boxes_needed = remaining_sq_ft / flooring_per_box
    result = boxes_needed
    return result

print(solution())
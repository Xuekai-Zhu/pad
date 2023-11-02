def solution():
    
    room_length = 16
    room_width = 20
    room_area = room_length * room_width
    flooring_per_box = 10
    flooring_already_laid = 250
    flooring_remaining = room_area - flooring_already_laid
    boxes_needed = flooring_remaining / flooring_per_box
    result = boxes_needed
    return result

print(solution())
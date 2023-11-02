def solution():
    """Tom was putting hardwood flooring into his living room that measured 16' long and 20' wide. The flooring comes 10 sq ft per box and he has already put down 250 sq ft of flooring. How many more boxes does Tom need to complete the job?"""
    living_room_area = 16 * 20
    flooring_per_box = 10
    flooring_put_down = 250
    flooring_needed = living_room_area - flooring_put_down
    boxes_needed = flooring_needed / flooring_per_box
    result = boxes_needed
    return result

print(solution())
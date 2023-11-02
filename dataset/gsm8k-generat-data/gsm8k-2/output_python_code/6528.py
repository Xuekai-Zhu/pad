def solution():
    """Tom was putting hardwood flooring into his living room that measured 16' long and 20' wide.
    The flooring comes 10 sq ft per box and he has already put down 250 sq ft of flooring.
    How many more boxes does Tom need to complete the job?"""
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
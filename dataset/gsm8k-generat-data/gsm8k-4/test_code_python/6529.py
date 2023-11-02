def solution():
    """Tom was putting hardwood flooring into his living room that measured 16' long and 20' wide.  The flooring comes 10 sq ft per box and he has already put down 250 sq ft of flooring.  How many more boxes does Tom need to complete the job?"""
    # Define the dimensions of the living room
    length = 16
    width = 20

    # Calculate the area of the living room
    area = length * width

    # Calculate the remaining area to be covered with flooring
    remaining_area = area - 250

    # Calculate the number of boxes needed to cover the remaining area
    boxes_needed = remaining_area / 10

    # Round up to the nearest whole number of boxes
    boxes_needed = int(boxes_needed + 0.5)

    result = boxes_needed
    return result

print(solution())
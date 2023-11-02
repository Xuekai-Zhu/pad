def solution():
    """Tom was putting hardwood flooring into his living room that measured 16' long and 20' wide.  The flooring comes 10 sq ft per box and he has already put down 250 sq ft of flooring.  How many more boxes does Tom need to complete the job?"""
    # Define the dimensions of the living room in feet
    length = 16
    width = 20

    # Calculate the total area of the living room in square feet
    total_area = length * width

    # Calculate the remaining area of the living room to be covered with flooring
    remaining_area = total_area - 250

    # Calculate the number of boxes of flooring needed to cover the remaining area
    boxes_needed = remaining_area / 10

    # Round up to the nearest whole number of boxes
    boxes_needed = math.ceil(boxes_needed)

    # Display the number of boxes needed
    result = boxes_needed
    return result

print(solution())
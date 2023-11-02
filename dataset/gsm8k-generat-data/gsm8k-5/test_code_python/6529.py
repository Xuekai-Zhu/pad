def solution():
    length = 16  # length of the room is 16 feet
    width = 20  # width of the room is 20 feet
    total_area = length * width  # total area of the room

    flooring_per_box = 10  # each box contains 10 sq ft of flooring
    flooring_laid = 250  # Tom has already put down 250 sq ft of flooring

    # Calculate the remaining area to be covered with new flooring
    remaining_area = total_area - flooring_laid

    # Calculate the number of boxes required to cover the remaining area
    boxes_required = remaining_area / flooring_per_box
    result = boxes_required
    return result

print(solution())
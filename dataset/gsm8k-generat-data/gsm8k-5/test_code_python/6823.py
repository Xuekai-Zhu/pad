def solution():
    initial_markers = 32  # Mr. Smith had 32 markers
    final_markers = 86  # After buying new boxes, Mr. Smith has 86 markers
    new_markers = final_markers - initial_markers  # Calculate the number of new markers Mr. Smith bought

    # Calculate the number of new boxes Mr. Smith bought
    new_boxes = new_markers // 9
    result = new_boxes
    return result

print(solution())
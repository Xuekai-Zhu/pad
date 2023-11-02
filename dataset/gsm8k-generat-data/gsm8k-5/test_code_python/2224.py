def solution():
    # Calculate the total number of cups in all the boxes
    total_cups = 26 * 5 * 4

    # Calculate the number of boxes that do not contain pans
    boxes_without_pans = 26 - 6

    # Calculate the number of boxes containing decorations
    boxes_with_decorations = boxes_without_pans / 2

    # Calculate the number of boxes containing teacups
    boxes_with_teacups = boxes_without_pans - boxes_with_decorations

    # Calculate the number of cups broken by Samuel
    cups_broken = boxes_with_teacups * 2

    # Calculate the number of cups left after Samuel takes them out of the boxes
    cups_left = total_cups - cups_broken
    result = cups_left
    return result

print(solution())
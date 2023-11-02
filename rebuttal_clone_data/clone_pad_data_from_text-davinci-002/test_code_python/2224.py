def solution():
    grandparents_teacups = 26 * 4 * 5
    boxes_of_pans = 6
    boxes_of_decorations = ((26 - 6) / 2)
    boxes_of_teacups = 26 - boxes_of_pans - boxes_of_decorations
    teacups_in_boxes = boxes_of_teacups * 4 * 5
    teacups_broken = ((26 * 4 * 5) / 2)
    total_teacups = grandparents_teacups - teacups_broken
    result = total_teacups
    return result

print(solution())
def solution():
    francine_boxes = 5  # Francine has 5 full boxes of crayons
    francine_loose = 5  # Francine has 5 loose crayons
    friend_loose = 27  # Francine's friend has 27 loose crayons
    total_crayons = 85  # Francine has a total of 85 crayons

    # Calculate the total number of loose crayons
    total_loose = francine_loose + friend_loose

    # Calculate the number of full boxes needed for the loose crayons
    boxes_needed = total_loose // 64  # Each box can hold 64 crayons

    # Calculate the number of remaining loose crayons
    remaining_loose = total_loose % 64

    # Calculate the total number of boxes needed
    total_boxes_needed = francine_boxes + boxes_needed
    if remaining_loose > 0:
        total_boxes_needed += 1

    # Calculate the number of boxes needed to reach the total number of crayons
    boxes_needed_for_total = (total_crayons - (francine_boxes * 64) - remaining_loose) // 64
    if (total_crayons - (francine_boxes * 64) - remaining_loose) % 64 > 0:
        boxes_needed_for_total += 1

    # Calculate the final number of boxes needed
    final_boxes_needed = total_boxes_needed + boxes_needed_for_total
    result = final_boxes_needed
    return result

print(solution())
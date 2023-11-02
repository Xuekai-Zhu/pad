def solution():
    """Francine has five full boxes of crayons and 5 loose crayons, and her friend has 27 loose crayons. They need to put all of their loose crayons in a box. How many more boxes do they need if Francine has a total of 85 crayons?"""
    francine_total_crayons = 85
    francine_full_boxes = 5
    francine_loose_crayons = 5
    friend_loose_crayons = 27
    total_loose_crayons = francine_loose_crayons + friend_loose_crayons
    total_crayons = francine_total_crayons + friend_loose_crayons
    total_boxes = francine_full_boxes + 1  # Add one more box for the loose crayons
    extra_boxes_needed = (total_boxes * 24) - total_crayons
    result = extra_boxes_needed
    return result

print(solution())
def solution():
    """Francine has five full boxes of crayons and 5 loose crayons, and her friend has 27 loose crayons. They need to put all of their loose crayons in a box. How many more boxes do they need if Francine has a total of 85 crayons?"""
    francine_full_boxes = 5
    francine_loose_crayons = 5
    friend_loose_crayons = 27
    total_crayons = francine_full_boxes * 20 + francine_loose_crayons + friend_loose_crayons
    total_boxes = total_crayons // 20
    extra_boxes = total_boxes - francine_full_boxes
    result = extra_boxes
    
    return result

print(solution())
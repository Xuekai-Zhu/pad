def solution():
    """Lucille is painting her room. Two of her walls are 3 meters wide and 2 meters tall. The third wall is 5 meters wide and 2 meters tall. The final wall is 4 meters wide and 2 meters tall. If each can of paint covers 2 square meters, how many cans of paint does Lucille need?"""
    wall1_area = 3 * 2
    wall2_area = 3 * 2
    wall3_area = 5 * 2
    wall4_area = 4 * 2
    total_area = wall1_area + wall2_area + wall3_area + wall4_area
    cans_needed = total_area / 2
    result = cans_needed
    return result

print(solution())
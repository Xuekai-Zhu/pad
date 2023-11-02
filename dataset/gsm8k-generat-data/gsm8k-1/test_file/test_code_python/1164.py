def solution():
    """The red rope was four times the length of the blue rope. The blue rope was 7 centimeters shorter than the yellow rope. If the 3 ropes had a combined length of 37 centimeters, what was the length of the red rope in centimeters?"""
    total_length = 37
    yellow_rope = (total_length - 7) / 2
    blue_rope = yellow_rope - 7
    red_rope = blue_rope * 4
    result = red_rope
    return result

print(solution())
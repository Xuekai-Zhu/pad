def solution():
    blankets_in_closet = 14  # Nathan has 14 blankets in his closet
    blankets_on_bed = blankets_in_closet / 2  # Nathan adds half of his blankets to his bed
    degrees_per_blanket = 3  # Each blanket warms Nathan up by 3 degrees

    # Calculate the total number of degrees the blankets warm Nathan up
    total_degrees = blankets_on_bed * degrees_per_blanket
    result = total_degrees
    return result

print(solution())
def solution():
    bear_cub_size = 8 # in inches
    king_size_bed_size = (76, 80) # in inches
    combined_width = bear_cub_size * 2
    combined_length = bear_cub_size
    if combined_width <= king_size_bed_size[0] and combined_length <= king_size_bed_size[1]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())
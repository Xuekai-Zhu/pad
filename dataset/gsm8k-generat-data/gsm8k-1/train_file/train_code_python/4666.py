def solution():
    """A 1165 cm long rope is cut into 154 pieces. 150 of the pieces are equally sized and the remaining pieces are 100mm each. Find the length of each of the equal pieces in millimeters."""
    total_length = 1165
    num_pieces = 154
    fixed_length = 100 # in mm
    var_length = (total_length - fixed_length * (num_pieces - 150)) / 150
    result = var_length * 10 # converting to mm
    return result

print(solution())
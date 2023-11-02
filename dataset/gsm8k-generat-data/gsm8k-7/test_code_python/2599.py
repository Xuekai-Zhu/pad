def solution():
    string_length = 15  # measured in feet
    wick_lengths = [6, 12]  # measured in inches

    # Convert string length to inches
    string_length_inches = string_length * 12

    # Calculate the number of wicks that can be cut from the string
    num_wicks = string_length_inches / sum(wick_lengths)

    # Calculate the total number of wicks after cutting
    num_6_inch_wicks = num_wicks * (wick_lengths[0] / sum(wick_lengths))
    num_12_inch_wicks = num_wicks * (wick_lengths[1] / sum(wick_lengths))
    total_num_wicks = num_6_inch_wicks + num_12_inch_wicks

    result = total_num_wicks
    return result

print(solution())
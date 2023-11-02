def solution():
    """Amy bought a 15-foot spool of string to cut up into wicks for making candles. If she cuts up the entire string into an equal number of 6-inch and 12-inch wicks, what is the total number of wicks she will have cut?"""
    # Initialize variables
    string_length = 15 * 12  # inches
    wick_length_1 = 6  # inches
    wick_length_2 = 12  # inches

    # Calculate the number of wicks of each type
    num_wicks_1 = string_length // wick_length_1
    num_wicks_2 = string_length // wick_length_2

    # Calculate the total number of wicks
    total_num_wicks = num_wicks_1 + num_wicks_2

    # Display the total number of wicks
    result = total_num_wicks
    return result

print(solution())
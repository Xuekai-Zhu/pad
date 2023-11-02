def solution():
    """If 100 pieces, each 15 centimeters long, are cut from a 51-meter long ribbon, how much ribbon remains ?"""
    # Define the length of the ribbon and the length of each cut piece
    ribbon_length = 51
    cut_length = 0.15

    # Calculate the total length of cut pieces
    total_cut_length = 100 * cut_length

    # Calculate the remaining length of ribbon
    remaining_length = ribbon_length - total_cut_length

    # return the result
    result = remaining_length
    return result

print(solution())
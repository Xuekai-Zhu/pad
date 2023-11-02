def solution():
    """If 100 pieces, each 15 centimeters long, are cut from a 51-meter long ribbon, how much ribbon remains?"""
    # Convert the length of the ribbon to centimeters
    ribbon_length = 5100

    # Calculate the total length of the pieces cut from the ribbon
    cut_length = 100 * 15

    # Calculate the remaining length of the ribbon
    remaining_length = ribbon_length - cut_length

    # Convert the remaining length back to meters
    remaining_length_meters = remaining_length / 100

    # Display the remaining length of the ribbon
    result = remaining_length_meters
    return result

print(solution())
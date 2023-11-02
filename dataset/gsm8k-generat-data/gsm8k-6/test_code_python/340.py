def solution():
    # Calculate the total length of rope needed
    total_length = 6 * 10  # one story is 10 feet
    length_with_loss = total_length / (1 - 0.25)  # accounting for the 25% loss
    num_pieces = length_with_loss / 20  # each piece of rope is 20 feet long
    result = math.ceil(num_pieces)  # round up to the nearest whole number
    return result

print(solution())
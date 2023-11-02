def solution():
    starting_length = 14  # Patricia's hair is currently 14 inches long
    desired_length = 12  # Patricia wants her hair to be 12 inches long after the donation
    required_donation = 23  # Patricia needs to donate 23 inches of hair to make a wig

    # Calculate how much longer Patricia needs to grow her hair to reach the desired length after donation
    additional_length_needed = desired_length + required_donation - starting_length
    result = additional_length_needed
    return result

print(solution())
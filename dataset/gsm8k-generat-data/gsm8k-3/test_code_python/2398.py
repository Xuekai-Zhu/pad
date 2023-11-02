def solution():
    """A piece of wire 5 feet 4 inches long was divided into 4 equal parts. How long was each part in inches if 1 foot is equal to 12 inches?"""
    # Convert the length of the wire into inches
    total_length = 5*12 + 4

    # Divide the total length into 4 equal parts
    part_length = total_length / 4

    # Convert the part length back into feet and inches
    part_feet = int(part_length / 12)
    part_inches = int(part_length % 12)

    # Display the length of each part in inches
    result = "{} inches".format(part_inches)
    return result

print(solution())
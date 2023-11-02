def solution():
    """A 40 meters rope was cut into 2 parts in the ratio of 2:3. How long is the shorter part?"""
    # Define the ratio of the rope's parts
    ratio = 2/3

    # Calculate the length of the shorter part
    shorter_part = (40*ratio)/(1+ratio)

    # Display the length of the shorter part
    result = shorter_part
    return result

print(solution())
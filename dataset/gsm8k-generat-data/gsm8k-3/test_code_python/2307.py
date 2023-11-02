def solution():
    """Josh wants to build a square sandbox that is 3 ft long, 3 ft wide for his son.  He can buy sand in 3 sq ft bags for $4.00 a bag.  How much will it cost him to fill up the sandbox?"""
    # Define the dimensions of the sandbox
    length = 3
    width = 3
    height = 0.5 # assuming a depth of 6 inches

    # Calculate the volume of sand needed
    volume = length * width * height

    # Calculate the number of bags needed
    bags = volume / 3

    # Calculate the total cost of the bags of sand
    cost = bags * 4

    # Display the total cost
    result = cost
    return result

print(solution())
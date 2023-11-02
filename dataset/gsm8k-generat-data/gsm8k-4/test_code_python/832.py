def solution():
    """John buys 1000 balloons. Each balloon holds 10 liters of air. If he buys 500-liter tanks of gas, how many tanks does he need to buy to fill all the balloons?"""
    # Define the number of balloons and the volume of each balloon
    balloons = 1000
    balloon_volume = 10

    # Calculate the total volume of air needed to fill all the balloons
    total_volume = balloons * balloon_volume

    # Calculate the number of tanks of gas needed to hold the total volume of air
    tanks_needed = total_volume / 500

    # Round up to the nearest integer to ensure all the balloons can be filled
    tanks_needed = math.ceil(tanks_needed)

    # return the result
    result = tanks_needed
    return result

print(solution())
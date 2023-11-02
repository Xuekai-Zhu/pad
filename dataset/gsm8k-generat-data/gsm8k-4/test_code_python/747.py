def solution():
    """John builds a model rocket that can travel 500 ft in the air. He builds a second rocket that can travel twice as high. What is the combined height of the two rockets?"""
    # Define the height of the first rocket
    rocket1_height = 500

    # Define the height of the second rocket, which is twice the height of the first rocket
    rocket2_height = rocket1_height * 2

    # Calculate the combined height of the two rockets
    combined_height = rocket1_height + rocket2_height

    # Return the result
    result = combined_height
    return result

print(solution())
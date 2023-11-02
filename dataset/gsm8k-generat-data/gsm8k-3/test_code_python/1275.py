def solution():
    """Ginger is weaving mats out of colored straw. Each mat takes 20 red straws, 30 orange straws, and half as many green straws as orange straws. How many straws does she need to make 10 mats?"""
    # Define the number of straws needed per mat
    RED_STRAWS_PER_MAT = 20
    ORANGE_STRAWS_PER_MAT = 30
    GREEN_STRAWS_PER_MAT = ORANGE_STRAWS_PER_MAT / 2

    # Define the number of mats to be made
    NUM_OF_MATS = 10

    # Calculate the total number of straws needed
    total_red_straws = RED_STRAWS_PER_MAT * NUM_OF_MATS
    total_orange_straws = ORANGE_STRAWS_PER_MAT * NUM_OF_MATS
    total_green_straws = GREEN_STRAWS_PER_MAT * NUM_OF_MATS
    total_straws = total_red_straws + total_orange_straws + total_green_straws

    # Display the total number of straws needed
    result = total_straws
    return result

print(solution())
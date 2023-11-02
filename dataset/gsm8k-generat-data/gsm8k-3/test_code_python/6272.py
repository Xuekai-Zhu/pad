def solution():
    """There are 5 green candies, 3 blue candies, and 4 red candies in a bag. If Violet randomly picks a candy from the bag, how likely is it that it's blue?"""
    # Define the total number of candies in the bag
    total_candies = 5 + 3 + 4

    # Calculate the probability of picking a blue candy
    blue_probability = 3 / total_candies

    # Display the probability of picking a blue candy
    result = blue_probability
    return result

print(solution())
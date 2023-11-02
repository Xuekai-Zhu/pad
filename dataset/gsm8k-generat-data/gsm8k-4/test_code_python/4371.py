def solution():
    """Jerry had 63 pieces of candy. He divided them up equally into 9 bags. 2 of the bags had chocolate hearts. 3 of the bags were chocolate kisses. The rest of the bags were not chocolate. How many pieces of candy were not chocolate?"""
    # Define the total number of candies and the number of bags
    total_candies = 63
    num_bags = 9

    # Calculate the number of candies in each bag
    candies_per_bag = total_candies / num_bags

    # Calculate the number of chocolate candies
    num_chocolate_candies = 2 * candies_per_bag + 3 * candies_per_bag

    # Calculate the number of non-chocolate candies
    num_non_chocolate_candies = total_candies - num_chocolate_candies

    # return the result
    result = num_non_chocolate_candies
    return result

print(solution())
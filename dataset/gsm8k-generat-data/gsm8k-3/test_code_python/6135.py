def solution():
    """A trader has 55 bags of rice in stock. She sells off some bags of rice and restocks 132 bags of rice. How many bags of rice did she sell if she now has 164 bags of rice?"""
    # Define the initial number of bags of rice
    initial_bags = 55

    # Define the final number of bags of rice
    final_bags = 164

    # Define the number of restocked bags
    restocked_bags = 132

    # Calculate the number of bags sold
    sold_bags = initial_bags + restocked_bags - final_bags

    # Display the number of bags sold
    result = sold_bags
    return result

print(solution())
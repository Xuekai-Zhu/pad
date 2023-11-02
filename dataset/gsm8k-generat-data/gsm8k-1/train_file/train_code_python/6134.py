def solution():
    """A trader has 55 bags of rice in stock. She sells off some bags of rice and restocks 132 bags of rice. How many bags of rice did she sell if she now has 164 bags of rice?"""
    starting_bags = 55
    restocked_bags = 132
    current_bags = 164
    sold_bags = starting_bags + restocked_bags - current_bags
    result = sold_bags
    return result

print(solution())
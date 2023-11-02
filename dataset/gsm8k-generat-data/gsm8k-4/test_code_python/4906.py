def solution():
    """Monroe has a collection of ants and a collection of spiders. He has 8 spiders and 12 ants. He is wondering what the number of legs of the entire collection is."""
    # Define the number of legs per ant and spider
    legs_per_ant = 6
    legs_per_spider = 8

    # Calculate the total number of legs for the ants
    ant_legs = 12 * legs_per_ant

    # Calculate the total number of legs for the spiders
    spider_legs = 8 * legs_per_spider

    # Calculate the total number of legs for the entire collection
    total_legs = ant_legs + spider_legs

    # Return the result
    return total_legs

print(solution())
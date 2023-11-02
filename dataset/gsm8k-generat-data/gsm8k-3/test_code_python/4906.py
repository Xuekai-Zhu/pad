def solution():
    """Monroe has a collection of ants and a collection of spiders. He has 8 spiders and 12 ants. He is wondering what the number of legs of the entire collection is."""
    # Define the number of legs for each type of insect
    SPIDER_LEGS = 8
    ANT_LEGS = 6

    # Calculate the total number of legs for the spiders
    spider_legs_total = 8 * SPIDER_LEGS

    # Calculate the total number of legs for the ants
    ant_legs_total = 12 * ANT_LEGS

    # Calculate the total number of legs for the entire collection
    total_legs = spider_legs_total + ant_legs_total

    # Display the total number of legs
    result = total_legs
    return result

print(solution())
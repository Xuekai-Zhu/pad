def solution():
    """Lisa has decided to replace her old cutlery. As she is going through the cupboards, she sees the spoons from when each of her 4 children were babies as well as 2 decorative spoons she created. She doesn't want to get rid of any of these so she adds them to her new set of cutlery. The new set of cutlery has 10 large spoons and 15 teaspoons. If the children each had 3 spoons when they were babies, how many spoons does Lisa now have?"""
    # Define the number of spoons from children and decorative spoons
    children_spoons = 4 * 3
    decorative_spoons = 2

    # Define the number of large and small spoons in the new set
    large_spoons = 10
    small_spoons = 15

    # Calculate the total number of spoons
    total_spoons = children_spoons + decorative_spoons + large_spoons + small_spoons

    result = total_spoons
    return result

print(solution())
def solution():
    """Lisa has decided to replace her old cutlery. As she is going through the cupboards, she sees the spoons from when each of her 4 children were babies as well as 2 decorative spoons she created. She doesn't want to get rid of any of these so she adds them to her new set of cutlery. The new set of cutlery has 10 large spoons and 15 teaspoons. If the children each had 3 spoons when they were babies, how many spoons does Lisa now have?"""
    # Calculate the total number of spoons from the children
    child_spoons = 4 * 3

    # Calculate the total number of spoons Lisa has after adding the old spoons and decorative spoons
    total_spoons = child_spoons + 2 + 10 + 15

    # Display the total number of spoons
    result = total_spoons
    return result

print(solution())
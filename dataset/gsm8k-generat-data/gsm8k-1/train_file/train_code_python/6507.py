def solution():
    """Lisa has decided to replace her old cutlery. As she is going through the cupboards, she sees the spoons from when each of her 4 children were babies as well as 2 decorative spoons she created. She doesn't want to get rid of any of these so she adds them to her new set of cutlery. The new set of cutlery has 10 large spoons and 15 teaspoons. If the children each had 3 spoons when they were babies, how many spoons does Lisa now have?"""
    num_children = 4
    num_baby_spoons = num_children * 3
    num_decorative_spoons = 2
    num_new_spoons = 10 + 15
    total_spoons = num_baby_spoons + num_decorative_spoons + num_new_spoons
    result = total_spoons
    return result

print(solution())
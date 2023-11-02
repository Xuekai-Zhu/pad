def solution():
    """Anna is making gingerbread cookies. She gives 6 of them red hats, 9 of them blue boots, and 3 of them both red hats and blue boots. What percentage of the gingerbread men have red hats?"""
    # Define the number of gingerbread men with red hats, blue boots, and both
    red_hats = 6
    blue_boots = 9
    both = 3

    # Calculate the number of gingerbread men with only red hats
    red_only = red_hats - both

    # Calculate the total number of gingerbread men
    total = red_only + blue_boots + both

    # Calculate the percentage of gingerbread men with red hats
    red_percentage = (red_only / total) * 100

    # Display the percentage of gingerbread men with red hats
    result = red_percentage
    return result

print(solution())
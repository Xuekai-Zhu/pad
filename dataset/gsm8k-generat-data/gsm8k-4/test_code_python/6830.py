def solution():
    """Anna is making gingerbread cookies. She gives 6 of them red hats, 9 of them blue boots, and 3 of them both red hats and blue boots. What percentage of the gingerbread men have red hats?"""
    # Calculate the total number of gingerbread men
    total_gingerbread_men = 6 + 9 - 3

    # Calculate the number of gingerbread men with red hats
    red_hats = 6 - 3

    # Calculate the percentage of gingerbread men with red hats
    percentage = (red_hats / total_gingerbread_men) * 100

    # return the result
    result = percentage
    return result

print(solution())
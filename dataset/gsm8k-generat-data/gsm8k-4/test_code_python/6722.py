def solution():
    """Yesterday, Vincent bought fifteen packs of stickers. Today, he bought ten more packs of stickers than yesterday. How many packs of stickers does Vincent have altogether?"""
    # Define the number of packs Vincent bought yesterday
    yesterday_packs = 15

    # Define the number of packs Vincent bought today
    today_packs = yesterday_packs + 10

    # Calculate the total number of packs Vincent has
    total_packs = yesterday_packs + today_packs

    # return the result
    result = total_packs
    return result

print(solution())
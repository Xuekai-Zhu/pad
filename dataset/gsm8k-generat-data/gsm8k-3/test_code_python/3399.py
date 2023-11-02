def solution():
    """On an American flag, the first stripe is red and half of the remaining stripes are also red. Each flag has 13 stripes.  John buys 10 flags.  How many red stripes are there?"""
    # Calculate the number of red stripes on one flag
    remaining_stripes = 12  # 13 total stripes - 1 red stripe
    red_stripes = 1 + (remaining_stripes // 2)  # 1 red stripe + half of remaining stripes
    # Calculate the total number of red stripes on 10 flags
    total_red_stripes = red_stripes * 10

    # Display the total number of red stripes
    result = total_red_stripes
    return result

print(solution())
def solution():
    """Theo, Mason, and Roxy are siblings.  Theo drinks 8 cups of water every day. Mason drinks 7 cups of water.  Roxy drinks 9 cups of water every day.  In one week, how many cups of water do the siblings drink together?"""
    # Define the daily water intake of each sibling
    theo_water = 8
    mason_water = 7
    roxy_water = 9

    # Calculate the total water intake of each sibling in one week
    theo_total = theo_water * 7
    mason_total = mason_water * 7
    roxy_total = roxy_water * 7

    # Calculate the total water intake of all the siblings in one week
    total_water = theo_total + mason_total + roxy_total

    # Display the total water intake
    result = total_water
    return result

print(solution())
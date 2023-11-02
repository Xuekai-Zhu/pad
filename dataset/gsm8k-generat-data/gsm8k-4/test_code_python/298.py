def solution():
    """There were sweets on the table. Jack came and took half of all the candies and 4 more candies. Then Paul came and took the remaining 7 sweets. How many sweets were on the table at first?"""
    # Let's assume that there were "x" sweets on the table initially

    # Jack took half of the sweets and 4 more
    jack_sweets = (x / 2) + 4

    # Remaining sweets after Jack took his share
    remaining_sweets = x - jack_sweets

    # Paul took the remaining 7 sweets
    paul_sweets = remaining_sweets - 7

    # Total sweets initially on the table
    total_sweets = jack_sweets + paul_sweets

    # Solving the equation for total sweets
    # jack_sweets + paul_sweets = remaining_sweets
    # jack_sweets + (remaining_sweets - 7) = remaining_sweets - jack_sweets - 4 - 7
    # jack_sweets = (remaining_sweets - 11) / 2
    # x/2 + 4 = (remaining_sweets - 11) / 2
    # x + 8 = remaining_sweets - 11
    # x = remaining_sweets - 19

    # Calculate the value of x
    x = total_sweets + 19

    result = x
    return result

print(solution())
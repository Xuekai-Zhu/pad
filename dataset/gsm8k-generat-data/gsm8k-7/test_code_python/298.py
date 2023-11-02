def solution():
    # Let's assume that there were "x" sweets on the table at first

    # Jack took half of all the candies and 4 more candies
    jack_sweets = (x / 2) + 4

    # After Jack took his share, there were "x/2 - 4" sweets left on the table
    remaining_sweets = x / 2 - 4

    # Paul took the remaining 7 sweets
    paul_sweets = 7

    # Total number of sweets on the table can be found by adding Jack's share, Paul's share, and remaining sweets
    total_sweets = jack_sweets + paul_sweets + remaining_sweets

    # We know that total_sweets should be equal to x, so we solve for x
    x = total_sweets

    return x

print(solution())
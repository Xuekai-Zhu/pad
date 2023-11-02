def solution():
    # Calculate the total amount of dollars Pete has
    total_dollars = 2 * 20 + 4 * 10  # Pete has two 20-dollar bills and four 10-dollar bills

    # Calculate how much more money Pete needs to pay off the bike
    remaining_dollars = 90 - total_dollars

    # Calculate how many bottles Pete needs to return to get the remaining dollars
    bottles = remaining_dollars / 0.5  # the store pays 50 cents per bottle

    result = bottles
    return result

print(solution())
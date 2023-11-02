def solution():
    total_screws = 8 * 3  # Mary needs to buy 2 times more screws, so she will have a total of 24 screws
    piles = 4  # Mary needs to split the screws into four sections

    # Calculate the number of screws in each pile
    screws_per_pile = total_screws / piles
    result = screws_per_pile
    return result

print(solution())
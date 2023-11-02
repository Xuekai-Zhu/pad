def solution():
    # Calculate the total number of screws Mary needs
    total_screws = 2 * 8  # Mary needs to buy 2 times more screws than she has

    # Calculate the number of screws in each pile
    screws_per_pile = total_screws / 4  # Mary splits the screws into four sections
    result = screws_per_pile
    return result

print(solution())
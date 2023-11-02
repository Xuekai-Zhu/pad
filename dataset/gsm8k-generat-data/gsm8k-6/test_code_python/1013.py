def solution():
    # Calculate the cost of the long-sleeved jerseys
    long_sleeve_cost = 4 * 15

    # Calculate the cost of the striped jerseys
    striped_cost = 80 - long_sleeve_cost

    # Calculate the number of striped jerseys bought
    striped_jerseys = striped_cost / 10

    result = striped_jerseys
    return result

print(solution())
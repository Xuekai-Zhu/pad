def solution():
    # Calculate the number of roses picked last year
    last_year_roses = 12

    # Calculate the number of roses picked this year
    this_year_roses = 0.5 * last_year_roses

    # Calculate the number of roses in the bouquet this year
    bouquet_roses = 2 * last_year_roses

    # Calculate the cost of the roses
    cost = bouquet_roses * 3

    result = cost
    return result

print(solution())
def solution():
    # Calculate the number of mountains that exploded in the first two months
    first_two_months = 0.2 * 200

    # Calculate the number of remaining mountains
    remaining = 200 - first_two_months

    # Calculate the number of mountains that exploded by the middle of the year
    by_half_year = 0.4 * remaining

    # Calculate the number of remaining mountains again
    remaining = remaining - by_half_year

    # Calculate the number of mountains that exploded at the end of the year
    end_of_year = 0.5 * remaining

    # Calculate the number of intact mountains at the end of the year
    intact_mountains = remaining - end_of_year
    result = intact_mountains
    return result

print(solution())
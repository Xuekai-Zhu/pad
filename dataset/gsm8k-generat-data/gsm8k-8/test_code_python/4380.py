def solution():
    # Define the ratio of selfies taken last year to this year
    last_year_to_this_year_ratio = 10/17

    # Calculate the total number of selfies
    total_selfies = 2430

    # Calculate the number of selfies taken last year
    last_year_selfies = total_selfies / (last_year_to_this_year_ratio + 1) * last_year_to_this_year_ratio

    # Calculate the number of selfies taken this year
    this_year_selfies = total_selfies - last_year_selfies

    # Calculate the difference in the number of selfies taken this year and last year
    difference = this_year_selfies - last_year_selfies
    result = difference
    return result

print(solution())
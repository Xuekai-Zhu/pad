def solution():
    """Gavin has had 4 dreams every day for a year now. If he had twice as many dreams last year as he had this year, calculate the total number of dreams he's had in the two years."""
    # Calculate the number of dreams Gavin had in a year
    current_year_dreams = 4 * 365

    # Calculate the number of dreams Gavin had last year
    last_year_dreams = current_year_dreams / 2

    # Calculate the total number of dreams Gavin had in the two years
    total_dreams = current_year_dreams + last_year_dreams

    # Display the total number of dreams
    result = total_dreams
    return result

print(solution())
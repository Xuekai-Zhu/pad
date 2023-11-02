def solution():
    # Find the total number of state quarters after each year
    year_1 = 50 * 2  # Doubled the 50 state quarters given by his parents
    year_2 = year_1 + (3 * 12)  # Collected 3 state quarters each month for a year
    year_3 = year_2 + (1 * 4)  # Collected 1 state quarter every third month for a year
    year_4 = int(year_3 * 0.75)  # Lost a quarter of the collection

    # Calculate the number of state quarters Phil has left
    remaining_quarters = year_4
    result = remaining_quarters
    return result

print(solution())
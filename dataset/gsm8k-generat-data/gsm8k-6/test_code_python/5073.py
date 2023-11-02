def solution():
    # Calculate the number of doughnuts sold
    num_doughnuts_sold = 27 * 10  # each box holds 10 doughnuts

    # Calculate the number of doughnuts left at the end of the day
    num_doughnuts_left = 300 - num_doughnuts_sold

    # Calculate the number of doughnuts given away
    num_doughnuts_given_away = num_doughnuts_left % 10

    result = num_doughnuts_given_away
    return result

print(solution())
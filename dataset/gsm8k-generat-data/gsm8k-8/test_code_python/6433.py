def solution():
    # Define the total number of crayons
    total_crayons = 48

    # Calculate the number of crayons Kiley takes away
    kiley_take_away = total_crayons / 4

    # Calculate the number of crayons remaining after Kiley's take away
    remaining_crayons = total_crayons - kiley_take_away

    # Calculate the number of crayons Joe takes away
    joe_take_away = remaining_crayons / 2

    # Calculate the final number of crayons remaining
    crayons_remaining = remaining_crayons - joe_take_away
    result = crayons_remaining
    return result

print(solution())